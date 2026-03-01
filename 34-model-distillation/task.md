# Model Distillation: Teacher Knows Best

## 🧠 Theory: Knowledge Distillation
Bigger isn't always better—sometimes smaller and faster is what we need! **Knowledge Distillation** allows a small "student" model to learn from a large "teacher" model. Instead of just training on the hard labels (0 or 1), the student learns to match the teacher's *logits* (soft targets). These logits contain rich information about the relationships between classes (e.g., a "Golden Retriever" is more like a "Labrador" than a "Truck").

## 🚀 The Assignment
You will build a distillation training loop. You'll create a teacher model (pre-trained/fixed) and a student model (smaller/trainable), and train the student to mimic the teacher.

### Steps
1.  **The Setup**: Define a `TeacherModel` (e.g., 3-layer MLP) and a `StudentModel` (e.g., 1-layer MLP or fewer neurons).
2.  **Soft Targets**: Implement a function to compute "soft targets" using softmax with a temperature $T$. $p_i = \frac{\exp(z_i/T)}{\sum \exp(z_j/T)}$. Higher $T$ makes the distribution softer.
3.  **The Loss**: Implement the combined loss:
    *   $L_{student} = \alpha \cdot L_{KL}(p_{student}, p_{teacher}) + (1-\alpha) \cdot L_{CE}(y_{student}, y_{true})$.
4.  **Training Loop**: Train the student on a dummy dataset (e.g., MNIST or generated points).
5.  **Compare**: Evaluate the student trained *with* distillation vs. a student trained *only* on hard labels. Did the teacher help?

## 🛠️ Tech Stack
- Python
- `torch`
- `torch.nn`
- `torch.nn.functional`

## 📦 Deliverables
1.  A script `distill.py` containing the models and training loop.
2.  A brief comparison of test accuracy between the distilled student and the baseline student.

## 🌟 Bonus Challenges (Optional)
- **Top-K Distillation**: Only distill the logits for the top-K classes to save computation/memory.
- **Intermediate Layer Distillation**: Can you force the student's hidden layers to match the teacher's hidden layers (using a projection matrix if dimensions differ)?
