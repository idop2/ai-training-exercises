# Text-to-Speech: Making Code Talk 📝➡️🔊

## 🧠 Theory: Mel-Spectrograms & Vocoders
Modern Text-to-Speech (TTS) pipelines generally consist of two main stages: an **Acoustic Model** (e.g., Tacotron, FastSpeech) that converts text into a Mel Spectrogram, and a **Vocoder** (e.g., WaveGlow, HiFi-GAN) that converts the spectrogram into a raw audio waveform. The key challenge is modeling the complex dependencies in speech (intonation, rhythm) and generating high-fidelity audio samples (usually 22kHz+).

## 🚀 The Assignment
You will build a simplified TTS pipeline. You'll focus on the Acoustic Model part: converting text characters/phonemes into a Mel Spectrogram. For the vocoder, you can use a pre-trained one (like HiFi-GAN) or implement a simple Griffin-Lim algorithm to turn your spectrograms into sound.

### Steps
1.  **Text Frontend**: Implement a text normalizer (convert "Mr." -> "Mister", "123" -> "one hundred twenty three") and a phonemizer (using `g2p_en` or similar) to convert raw text into phoneme sequences.
2.  **The Acoustic Model**: Build a model (e.g., a simple Tacotron-like encoder-decoder with attention, or a FastSpeech-like non-autoregressive transformer) that predicts 80-channel Mel Spectrogram frames from phonemes.
3.  **Training**: Train your model on a single-speaker dataset like LJSpeech (or a small subset). The loss function is typically MSE or L1 between predicted and ground-truth spectrograms.
4.  **Vocoding**: Use a pre-trained vocoder (available in `torchaudio` or similar libraries) or Griffin-Lim to synthesize audio from your predicted spectrograms.

## 🛠️ Tech Stack
- **PyTorch**: For the model.
- **Torchaudio**: For spectrograms and vocoders.
- **Phonemizer** (or `g2p_en`): For text processing.
- **Librosa**: For audio I/O.

## 📦 Deliverables
1.  `text.py`: Text normalization and phonemization functions.
2.  `model.py`: Your acoustic model architecture.
3.  `synthesize.py`: A script that takes a string of text and saves a `.wav` file.

## 🌟 Bonus Challenges (Optional)
- **FastSpeech Implementation**: Instead of an autoregressive model (like Tacotron), implement a non-autoregressive one (like FastSpeech) which predicts duration for each phoneme.
- **Multi-Speaker**: Condition the model on a speaker embedding (d-vector) to change the voice identity.
