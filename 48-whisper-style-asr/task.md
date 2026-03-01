# Whisper-Style ASR: Sequence-to-Sequence Speech 🗣️➡️📝

## 🧠 Theory: Encoder-Decoder & Log-Mel
Automatic Speech Recognition (ASR) is the task of transcribing spoken language into text. Modern systems like OpenAI's Whisper treat this as a sequence-to-sequence problem. An **Encoder** processes the audio features (Log-Mel Spectrograms) into a rich representation, and a **Decoder** (like GPT) autoregressively predicts the text tokens, attending to the encoder's output. Whisper's secret sauce also includes multitasking (translation, language ID) and special tokens for timestamps.

## 🚀 The Assignment
You will implement a simplified version of the Whisper architecture. You'll build the Encoder-Decoder Transformer and the specific preprocessing pipeline required to feed it. Your goal is to train (or fine-tune) a small model to transcribe short audio clips.

### Steps
1.  **The Audio Frontend**: Implement the specific Log-Mel Spectrogram calculation used by Whisper (80 mel bands, 25ms window).
2.  **The Encoder**: A Transformer Encoder with two 1D convolution layers at the start (the "stem") to downsample the time dimension.
3.  **The Decoder**: A Transformer Decoder that attends to the Encoder's output (Cross-Attention) and the previously generated tokens (Self-Attention).
4.  **The Loop**: Write the inference loop. It's `generated_tokens = [START]`, then loop: `logits = model(audio, generated_tokens)`, `next_token = sample(logits)`, `append`.

## 🛠️ Tech Stack
- **PyTorch**: For the model.
- **Torchaudio**: For spectrograms.
- **Hugging Face Tokenizers**: To use the BPE tokenizer (likely GPT-2's or Whisper's).

## 📦 Deliverables
1.  `whisper_model.py`: Your implementation of the Encoder-Decoder architecture.
2.  `transcribe.py`: A script that takes an audio file path, runs the model, and prints the text.
3.  `comparison.md`: Compare your implementation's architecture details (layer norms, activation functions) with the official OpenAI code/paper.

## 🌟 Bonus Challenges (Optional)
- **KV Caching**: Implement Key-Value caching in the decoder to speed up inference significantly.
- **Timestamps**: Add the ability to predict timestamp tokens (e.g., `<|0.00|>`, `<|1.50|>`) to align text with audio.
