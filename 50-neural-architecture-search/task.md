# Neural Architecture Search: The AI That Builds AI 🤖🏗️

## 🧠 Theory: Search Spaces & Controllers
Designing neural networks by hand is tedious. Neural Architecture Search (NAS) automates this. We define a **Search Space** (e.g., "Number of layers: [1-10]", "Kernel size: [3, 5, 7]", "Activation: [ReLU, SiLU]") and use a **Search Algorithm** (Reinforcement Learning, Evolution, or Differentiable Search like DARTS) to find the best configuration. The "Controller" proposes an architecture, we train it (or estimate its accuracy), and the feedback improves the controller.

## 🚀 The Assignment
You will implement a basic NAS system to find the optimal Convolutional Neural Network (CNN) architecture for CIFAR-10. Instead of training every candidate from scratch (which is slow), you'll implement a "Weight Sharing" approach (like ENAS/DARTS) or a simple evolutionary algorithm with a small budget.

### Steps
1.  **The Supernet**: Define a massive "Supernet" that contains *all* possible operations (e.g., multiple branches with different kernel sizes). The search will involve selecting which paths to keep.
2.  **The Search Space**: Define the choices (e.g., Layer 1: Conv3x3 or Conv5x5? Layer 2: MaxPool or AvgPool?).
3.  **The Controller**: Implement a search strategy.
    - *Option A (Evolution)*: Randomly initialize a population of architectures. Mutate them (flip an op). Train for 1 epoch. Keep the best. Repeat.
    - *Option B (RL)*: An LSTM controller predicts the architecture string. Train the child network. Use accuracy as reward to update the controller.
4.  **Evaluation**: Run the search for a few hours/iterations. Take the best architecture found and train it fully from scratch to verify its performance.

## 🛠️ Tech Stack
- **PyTorch**: Dynamic graphs make defining search spaces easier.
- **Ray Tune** (optional): Great for hyperparameter search if you want a robust library, but try building the loop yourself first!

## 📦 Deliverables
1.  `search_space.py`: Definition of your operations and the supernet.
2.  `search.py`: The script running the NAS algorithm (Evolution/RL).
3.  `best_arch.json`: The configuration of the winning architecture.

## 🌟 Bonus Challenges (Optional)
- **DARTS**: Implement Differentiable Architecture Search, where you relax the categorical choices into continuous weights (softmax) and optimize them with gradient descent.
- **Hardware-Aware NAS**: Add a latency constraint (e.g., "Must run under 10ms on CPU") to the reward function.
