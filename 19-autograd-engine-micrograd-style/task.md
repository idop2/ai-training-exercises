# Autograd Engine: Build Your Own Micrograd!

## 🧠 Theory: The Heart of Deep Learning
Deep Learning frameworks like PyTorch and TensorFlow seem like magic, but at their core is a concept called **Automatic Differentiation** (Autograd). It's the engine that calculates gradients—how much each parameter contributed to the error—so we can adjust them. Building an autograd engine from scratch is the single best way to demystify neural networks. You'll stop seeing "black boxes" and start seeing mathematical graphs.

## 🚀 The Assignment
You will build a scalar-valued autograd engine (inspired by Andrej Karpathy's `micrograd`).

### Steps
1.  **The `Value` Object**: Create a class that wraps a single number. It needs to store:
    *   The `data` (the value itself).
    *   The `grad` (the derivative, initialized to 0).
    *   The `_backward` (a function to propagate gradients).
    *   The `_prev` (children nodes in the graph).
2.  **Operations**: Implement the basic arithmetic operations (`__add__`, `__mul__`, `__pow__`, `__relu__`) for your `Value` class.
    *   *Crucial*: Each operation must define its own `_backward` function to implement the Chain Rule!
3.  **Backpropagation**: Implement a `.backward()` method that sorts the graph topologically and calls `_backward()` on each node in reverse order.
4.  **The Neuron**: Use your `Value` class to build a `Neuron` (weights * inputs + bias), then a `Layer`, and finally an `MLP` (Multi-Layer Perceptron).
5.  **Training**: Train your MLP to solve a simple problem (like XOR or a simple regression) using gradient descent.

## 🛠️ Tech Stack
- **Python** (Standard library only! No PyTorch/TensorFlow allowed for the engine logic.)
- **Graphviz** (optional, for visualizing the computation graph)

## 📦 Deliverables
1.  `autograd.py`: Your engine implementation.
2.  `train.py`: A script that creates a small neural network using your engine and trains it on dummy data.
3.  `loss_plot.png`: A plot showing the loss going down over time.

## 🌟 Bonus Challenges
- **Add More Ops**: Implement `tanh`, `exp`, or `sigmoid`.
- **PyTorch Comparison**: Write a test that compares your gradients against PyTorch's gradients to prove they are identical.
