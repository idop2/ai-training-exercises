# Vision Transformer (ViT): Images are Just Words 🟦🟩🟥

## 🧠 Theory: Patchify & Self-Attention
For years, Convolutional Neural Networks (CNNs) ruled computer vision. The Vision Transformer (ViT) challenged this by treating an image not as a grid of pixels, but as a sequence of patches (e.g., 16x16 squares). It flattens these patches, projects them, adds position embeddings, and feeds them into a standard Transformer Encoder. It turns out, if you have enough data, attention is all you need for images too!

## 🚀 The Assignment
You will implement the original Vision Transformer (ViT) architecture from scratch. You'll build the patch embedding layer, the transformer encoder blocks, and the classification head, then train it on a classic dataset like CIFAR-10.

### Steps
1.  **Patch Embeddings**: Implement a module that takes an image (H x W x C) and chops it into $N$ patches, flattening them into vectors. A Conv2d layer with `kernel_size=patch_size` and `stride=patch_size` is a clever trick for this!
2.  **The Transformer**: Build the standard Transformer Encoder (Multi-Head Self-Attention + MLP + LayerNorm + Residual Connections).
3.  **The Class Token**: Prepend a learnable `[CLS]` token to the sequence of patch embeddings. This token's final state will represent the entire image for classification.
4.  **Position Embeddings**: Add learnable position embeddings to the sequence so the model knows which patch is where.

## 🛠️ Tech Stack
- **PyTorch**: The deep learning framework.
- **Einops**: *Highly* recommended for the "patchify" operation (e.g., `rearrange(images, 'b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1=patch_size, p2=patch_size)`).
- **Torchvision**: For downloading CIFAR-10/MNIST.

## 📦 Deliverables
1.  `vit.py`: Your complete `VisionTransformer` class.
2.  `train.py`: A training script achieving reasonable accuracy (>60-70%) on CIFAR-10.
3.  `attention_map.png`: A visualization of the attention weights for a few test images (which patches attend to which?).

## 🌟 Bonus Challenges (Optional)
- **Masked Autoencoder (MAE)**: Modify your ViT to randomly mask 75% of the patches and try to reconstruct the missing pixels.
- Compare the learnable position embeddings vs. fixed sinusoidal embeddings.
