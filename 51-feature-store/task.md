# Feature Store: The Data Supply Chain 🏪

## 🧠 Theory: Online vs. Offline & Point-in-Time
In production ML, the data used for training (historical, offline) must match the data used for inference (real-time, online). A **Feature Store** solves the "training-serving skew." It manages feature definitions, computes them consistently, and serves them via two APIs:
1.  **Offline API**: Returns historical features for training (handling point-in-time correctness so you don't leak future data).
2.  **Online API**: Returns the latest feature values at low latency for real-time prediction.

## 🚀 The Assignment
You will build a mini Feature Store. You won't use a heavy tool like Tecton or Feast directly; you'll implement the core logic yourself to understand how they work. You'll support defining features, ingesting data, and retrieving it for both training and serving.

### Steps
1.  **The Registry**: Create a way to define "Feature Views" (e.g., a YAML file or Python class defining `user_clicks_last_7d`).
2.  **Ingestion**: Write a function to ingest a DataFrame of raw events (e.g., `click_logs`) and compute the feature values. Store them in two places:
    - **Offline Store**: A Parquet file or SQL table (append-only).
    - **Online Store**: A Key-Value store (like Redis or a Python dict for simulation) holding only the *latest* value.
3.  **Offline Retrieval (Time Travel)**: Implement `get_historical_features(entity_df)`. For each row in `entity_df` (user_id, timestamp), find the feature value *as it was known at that timestamp*.
4.  **Online Retrieval**: Implement `get_online_features(entity_ids)`. Fetch the current values from the KV store immediately.

## 🛠️ Tech Stack
- **Pandas**: For data manipulation and the offline store.
- **Redis** (optional): For the online store (or just use a dictionary/SQLite).
- **Feast** (reference): Look at Feast's documentation for inspiration on API design.

## 📦 Deliverables
1.  `feature_store.py`: The core class managing the registry and stores.
2.  `definitions.py`: A sample feature definition file.
3.  `demo.ipynb`: A notebook showing ingestion, training data generation (checking for correctness), and online serving.

## 🌟 Bonus Challenges (Optional)
- **Entity Resolution**: Handle joining features from different entities (e.g., `User` features + `Item` features) in one request.
- **Streaming Ingestion**: Update the online store in real-time as new events arrive (simulated).
