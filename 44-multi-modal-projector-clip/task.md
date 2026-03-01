# Multi-Modal Projector: Teaching Images to Speak 🖼️🗣️

## 🧠 Theory: CLIP & Projection Layers
How do models understand that a photo of a cat and the word "cat" are related? They map them into a shared vector space where similar concepts are close together. Models like CLIP use separate encoders for text (e.g., Transformer) and images (e.g., ResNet/ViT). A "Projection Layer" (often just a linear layer or MLP) transforms the output of each encoder into this shared dimension. Training aligns these projections using "Contrastive Loss"—pulling matching pairs together and pushing mismatched ones apart.

## 🚀 The Assignment
You will build a "Multi-Modal Projector" to align text and image embeddings. You'll take pre-trained encoders (frozen), add trainable projection heads, and implement the CLIP training loop on a small image-caption dataset.

### Steps
1.  **The Encoders**: Load a pre-trained Image Encoder (e.g., ResNet50 or ViT-B/32) and a Text Encoder (e.g., DistilBERT). Freeze their weights.
2.  **The Projectors**: Implement two small neural networks (MLPs) that take the encoder outputs (e.g., 768-dim) and project them to a shared embedding dimension (e.g., 256-dim).
3.  **Contrastive Loss**: Implement the InfoNCE loss function. For a batch of $N$ image-text pairs, maximize the similarity of the $N$ correct pairs while minimizing the similarity of the $N^2 - N$ incorrect pairings.
4.  **Training Loop**: Train the projectors on a dataset like COCO or Flickr8k (or a small subset).

## 🛠️ Tech Stack
- **PyTorch**: For the model and training loop.
- **Hugging Face Transformers**: To load the pre-trained encoders.
- **Torchvision**: For image transforms.

## 📦 Deliverables
1.  `model.py`: A `CLIPModel` class wrapping the encoders and your projection layers.
2.  `train.py`: The training script with the contrastive loss implementation.
3.  `inference.ipynb`: A notebook where you input an image and retrieve the most relevant caption from a list, demonstrating the alignment.

## 🌟 Bonus Challenges (Optional)
- Implement "Zero-Shot Classification": Use your aligned model to classify images by comparing their embeddings to the embeddings of class names ("a photo of a dog", "a photo of a car").
- Visualizing the attention: If using a ViT, visualize which parts of the image the model focuses on for specific words.
