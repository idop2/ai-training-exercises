# Diffusion Models: From Noise to Art 🎨

## 🧠 Theory: Denoising & The Forward Process
Diffusion models (like Stable Diffusion) work by gradually adding Gaussian noise to an image until it's pure static (the "forward process"). Then, they learn to reverse this: taking pure noise and predicting *how much noise* was added at each step, iteratively "denoising" it back into a coherent image. The core components are a **UNet** (to predict the noise) and a **Scheduler** (to control the noise schedule).

## 🚀 The Assignment
You will implement the two main pillars of a diffusion model: the Noise Scheduler (managing the variance $\beta_t$) and a simple UNet (to predict the noise). You'll train this on a toy dataset (like MNIST or even 2D points) to generate samples from scratch.

### Steps
1.  **The Scheduler**: Implement a class (e.g., `DDPMScheduler` or `DDIMScheduler`) that handles:
    - Adding noise to an image at time $t$ (`add_noise(x_0, noise, t)`).
    - Calculating the $\alpha_t, \bar{\alpha}_t, \sigma_t$ coefficients needed for the forward/backward pass.
2.  **The UNet**: Build a small UNet architecture with residual blocks and (optionally) time embeddings. The input is a noisy image + time step; the output is the predicted noise.
3.  **Training**: Sample random timesteps $t$, add noise to your data, run it through the UNet, and minimize the Mean Squared Error (MSE) between the *actual* noise and the *predicted* noise.
4.  **Generation**: Implement the sampling loop. Start with pure Gaussian noise and iteratively denoise using your trained UNet and Scheduler.

## 🛠️ Tech Stack
- **PyTorch**: For the neural network.
- **Diffusers** (optional reference): Hugging Face's library is the gold standard; try implementing your own scheduler first, then compare.
- **Matplotlib**: To visualize the denoising process step-by-step.

## 📦 Deliverables
1.  `scheduler.py`: Your noise scheduler implementation.
2.  `unet.py`: The UNet model definition.
3.  `train.py`: The training loop.
4.  `sample.gif`: An animation showing the reverse process (noise $\to$ image).

## 🌟 Bonus Challenges (Optional)
- Implement **Classifier-Free Guidance**: Train the model with class labels (or drop them randomly) and use guidance scale $>1$ during sampling to control the generation.
- Implement a faster sampler like **DDIM** or **Euler Discrete** to generate images in fewer steps (e.g., 20 instead of 1000).
