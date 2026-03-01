# Distributed Training: Divide and Conquer with FSDP & TP

## 🧠 Theory: Scaling Beyond One GPU
Modern LLMs are too big for a single GPU. We need strategies to split them up!
*   **FSDP (Fully Sharded Data Parallel)**: Instead of replicating the whole model on every GPU (standard DDP), FSDP shards the model parameters, gradients, and optimizer states across GPUs. It gathers them only when needed for computation.
*   **TP (Tensor Parallelism)**: Splits individual large matrix multiplications across GPUs. It's like slicing a big matrix into chunks, computing on each chunk in parallel, and stitching the results back.

## 🚀 The Assignment
You will gain hands-on experience with PyTorch's FSDP wrapper. Since you might not have a multi-GPU cluster, we'll focus on setting up the architecture and understanding the API using a script that *could* run distributed, or by simulating it if possible (though FSDP typically requires a distributed environment, you can write the code to be ready for it).

*Note: If you don't have multiple GPUs, you can verify your script runs on CPU/single GPU without crashing, but the true "sharding" benefits happen in a distributed context.*

### Steps
1.  **Define a Simple Model**: Create a PyTorch `nn.Module` with a few large `nn.Linear` layers.
2.  **Initialize Process Group**: Set up `dist.init_process_group` (use `backend='gloo'` or `nccl`).
3.  **Wrap with FSDP**: Use `torch.distributed.fsdp.FullyShardedDataParallel` to wrap your model.
4.  **Inspect the Model**: Print the model structure after wrapping. Notice how layers are replaced or wrapped.
5.  **Dummy Train Step**: Run a forward pass, backward pass, and optimizer step with dummy data.

## 🛠️ Tech Stack
- Python
- `torch`
- `torch.distributed`

## 📦 Deliverables
1.  A script `fsdp_train.py` that sets up a distributed environment (or simulates it) and wraps a model in FSDP.
2.  Output logs showing the wrapped model architecture.

## 🌟 Bonus Challenges (Optional)
- **Mixed Precision**: Configure FSDP to use `float16` or `bfloat16` for parameters.
- **Manual TP**: Implement a manual "Tensor Parallel" Linear layer that splits the weight matrix into two chunks (conceptually) and performs the matmul.
