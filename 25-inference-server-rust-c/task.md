# Inference Server: High-Performance Serving with Rust/C++!

## 🧠 Theory: Moving to Production
Python is the language of research, but **C++** and **Rust** are the languages of production inference. When you need to serve a model to millions of users, overhead matters. Python's Global Interpreter Lock (GIL) and dynamic typing can be bottlenecks. Learning to load and serve a model in a lower-level language is a critical skill for MLOps and systems engineers.

## 🚀 The Assignment
You will build a high-performance REST API in Rust (or C++) that serves a pre-trained ONNX model.

### Steps
1.  **The Model**: Export a simple model (e.g., a ResNet or a simple text classifier) to **ONNX** format using Python.
2.  **The Runtime**: Use `ort` (Rust bindings for ONNX Runtime) or the C++ ONNX Runtime API to load the model file.
3.  **The Server**: Set up a web server.
    *   **Rust**: Use `Actix-web` or `Axum`.
    *   **C++**: Use `Crow` or `Drogon`.
4.  **The Endpoint**: Create a `/predict` endpoint that:
    *   Accepts JSON payload (input tensors).
    *   Converts JSON to the runtime's tensor format.
    *   Runs inference.
    *   Returns the results as JSON.

## 🛠️ Tech Stack
- **Language**: Rust (Recommended) or C++.
- **Library**: ONNX Runtime.
- **Web Framework**: Actix/Axum (Rust) or Crow (C++).

## 📦 Deliverables
1.  `convert_model.py`: Python script to save a dummy model as `.onnx`.
2.  `main.rs` (or `.cpp`): The source code for your inference server.
3.  `Cargo.toml` (or `CMakeLists.txt`): Build configuration.
4.  `benchmark.md`: Use a tool like `wrk` or `Apache Bench` to hit your API and record the requests per second.

## 🌟 Bonus Challenges
- **Batched Inference**: Modify your server to accept a batch of inputs and process them in a single model run for higher throughput.
- **Dockerize**: Wrap your compiled binary in a tiny Docker container (distroless) for deployment.
