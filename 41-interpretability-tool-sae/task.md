# Interpretability with SAEs: X-Raying the Model 🔍

## 🧠 Theory: Sparse Autoencoders (SAEs)
Neural networks are notoriously opaque "black boxes." We see the output, but not *how* they thought of it. Activation patterns in the hidden layers are dense and polysemantic (one neuron fires for many unrelated concepts). Sparse Autoencoders (SAEs) decompose these messy activations into sparse, interpretable "features." It's like taking a mixed smoothie (the activation) and un-blending it back into distinct fruits (the features).

## 🚀 The Assignment
You will build a tool to interpret a small language model (like GPT-2 Small or TinyLlama). You'll extract activations, train a Sparse Autoencoder to reconstruct them, and then visualize what specific "features" the SAE has learned.

### Steps
1.  **Harvest Activations**: Write a script to run text through a pre-trained model (e.g., from Hugging Face) and save the activations from a specific MLP layer.
2.  **Build the SAE**: Implement a Sparse Autoencoder. It should have an encoder (activations $\to$ sparse features) and a decoder (sparse features $\to$ reconstructed activations), trained with an L1 penalty to encourage sparsity.
3.  **Train the SAE**: Train your autoencoder on the harvested activations. Monitor the "dead neuron" percentage (features that never fire).
4.  **Feature Visualization**: Find the text snippets that maximally activate specific SAE features. Can you find a "grammar" feature? A "Harry Potter" feature?

## 🛠️ Tech Stack
- **PyTorch**: For the autoencoder and model handling.
- **TransformerLens** (optional but recommended) or **Hugging Face Transformers**: To hook into the model and extract activations.
- **Datasets**: To load a text corpus (like OpenWebText or a subset).

## 📦 Deliverables
1.  `sae.py`: Your Sparse Autoencoder class definition.
2.  `train_sae.py`: Script to train the SAE on model activations.
3.  `interpret.ipynb`: A notebook exploring the learned features, showing examples of text that triggers them.

## 🌟 Bonus Challenges (Optional)
- Implement "ghost grads" or other techniques to reduce dead neurons during training.
- Use your SAE to "steer" the model by clamping a specific feature (e.g., make the model obsessed with "golden retrievers").
