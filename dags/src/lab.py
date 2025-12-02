import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import pickle
import os
import base64

def load_data():
    """
    Loads employee productivity dataset and returns a base64 string.
    """
    print("Loading Employee Productivity Data...")
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/employee_productivity.csv"))

    serialized_data = pickle.dumps(df)
    return base64.b64encode(serialized_data).decode("ascii")


def data_preprocessing(data_b64: str):
    """
    Preprocesses Employee Productivity Dataset.
    Uses only numeric columns suitable for clustering.
    """

    data_bytes = base64.b64decode(data_b64)
    df = pickle.loads(data_bytes)

    df = df.dropna()

    # Select numeric features for clustering
    features = ["experience_years","hours_per_week","tasks_completed","efficiency_score"]
    clustering_data = df[features]

    scaler = MinMaxScaler()
    clustering_scaled = scaler.fit_transform(clustering_data)

    serialized = pickle.dumps(clustering_scaled)
    return base64.b64encode(serialized).decode("ascii")


def build_save_model(data_b64: str, filename: str):
    """
    Runs KMeans for k=1–10 and saves the LAST model.
    Returns the SSE values list.
    """

    data_bytes = base64.b64decode(data_b64)
    df = pickle.loads(data_bytes)

    kmeans_kwargs = {"init": "random", "n_init": 10, "max_iter": 300, "random_state": 42}

    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
        kmeans.fit(df)
        sse.append(kmeans.inertia_)

    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)

    with open(output_path, "wb") as f:
        pickle.dump(kmeans, f)

    return sse


def load_model_elbow(filename: str, sse: list):
    """
    Loads saved model and returns 1 prediction.
    """

    model_path = os.path.join(os.path.dirname(__file__), "../model", filename)
    model = pickle.load(open(model_path, "rb"))

    kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")
    print(f"Optimal K = {kl.elbow}")

    df_test = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/employee_productivity.csv"))

    # Use first row
    pred = model.predict(df_test[["experience_years","hours_per_week","tasks_completed","efficiency_score"]])[0]

    return int(pred)
