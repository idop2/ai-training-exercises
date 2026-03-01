# Audio Spectrogram Transformer: Seeing Sound 🎵👁️

## 🧠 Theory: Spectrograms & Patchify
Audio is temporal (1D signal), but we can visualize it as an image using a **Spectrogram** (time on X-axis, frequency on Y-axis). Once audio is an "image," we can apply powerful Vision techniques! The Audio Spectrogram Transformer (AST) does exactly this: it takes a spectrogram, chops it into patches, adds position embeddings, and feeds it into a standard Transformer Encoder for classification. It's ViT for your ears.

## 🚀 The Assignment
You will build an end-to-end pipeline to classify audio clips. You'll convert raw waveforms into Mel Spectrograms, patchify them, and train a Transformer to recognize the sounds (e.g., "dog barking", "siren", "rain").

### Steps
1.  **Preprocessing**: Write a function to load audio files (e.g., `.wav`), resample them, and convert them into Log-Mel Spectrograms using `torchaudio`. Normalize them to be model-friendly (mean 0, std 1).
2.  **Patch Embedding**: Adapt the ViT patch embedding logic to work on these spectrograms. Note: Spectrograms have variable lengths (time) but fixed height (frequency bins). You might need to crop/pad to a fixed size.
3.  **The Transformer**: Use a standard Transformer Encoder (or reuse your ViT implementation!).
4.  **Classification Head**: Add a linear layer on top of the `[CLS]` token to predict the class of the audio.
5.  **Training**: Train on a subset of AudioSet or ESC-50.

## 🛠️ Tech Stack
- **PyTorch**: For the model.
- **Torchaudio**: Essential for loading and transforming audio.
- **Librosa** (optional): Another great audio library.

## 📦 Deliverables
1.  `data.py`: A dataset class that loads audio and returns spectrogram tensors.
2.  `ast.py`: The Audio Spectrogram Transformer model.
3.  `train.py`: Training script for audio classification.

## 🌟 Bonus Challenges (Optional)
- **Masking**: Implement "SpecAugment" (masking time or frequency bands) during training to make the model robust.
- **Variable Length**: Modify the model to handle audio clips of different durations without excessive padding (maybe using attention masks).
