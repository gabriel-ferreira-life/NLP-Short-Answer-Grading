# 🧠 Fine-tuned LLaMA 3.2-3B Instruct for Short Answer Classification

This project fine-tunes the [LLaMA 3.2-3B Instruct model](https://huggingface.co/Gabriel-Ferreira/Llama-3.2-3B-Instruct-Short-Answer-Classification) to grade short-answer responses in educational settings. The model classifies student answers into three categories: **Correct**, **Partially Correct**, or **Incorrect**.

---

## 🚀 Model Overview

- **Base Model**: LLaMA 3.2-3B Instruct  
- **Task**: Short Answer Grading (3-Class Classification)  
- **Classes**: `"Correct"`, `"Partially Correct"`, `"Incorrect"`  
- **Training Method**: Parameter-Efficient Fine-Tuning with LoRA (Low-Rank Adaptation)

---

## 🧾 Prompt Format

The model expects the following input structure:

```
Classify the student response into Correct, Partially Correct, or Incorrect, and return the answer as the corresponding answer label.
Question: <question>
Response: <student_response>
Correct Answer: <expected_answer>
label:
```

The model will complete the prompt with one of: 
```
Correct
Partially Correct
Incorrect
```

---

## 📦 Model Access

The fine-tuned model is available on the Hugging Face Hub:

👉 [Gabriel-Ferreira/Llama-3.2-3B-Instruct-Short-Answer-Classification](https://huggingface.co/Gabriel-Ferreira/Llama-3.2-3B-Instruct-Short-Answer-Classification)

You can load it using:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Gabriel-Ferreira/Llama-3.2-3B-Instruct-Short-Answer-Classification")
tokenizer = AutoTokenizer.from_pretrained("Gabriel-Ferreira/Llama-3.2-3B-Instruct-Short-Answer-Classification")
```

---

## 📊 Evaluation

The model was evaluated on a test set containing 30,466 observations. The performance metrics for each class are as follows:

- **Correct:** 94.0% accuracy  
- **Partially Correct:** 35.3% accuracy  
- **Incorrect:** 96.5% accuracy  

### Classification Report

| **Label**           | **Precision** | **Recall** | **F1-Score** | **Support** |
|---------------------|---------------|------------|--------------|-------------|
| Correct             | 0.97          | 0.94       | 0.95         | 13,532      |
| Partially Correct   | 0.16          | 0.35       | 0.22         | 320         |
| Incorrect           | 0.97          | 0.97       | 0.97         | 16,614      |

- **Overall Accuracy:** 95.0%
- **Macro Average:** Precision = 0.70, Recall = 0.75, F1-Score = 0.71  
- **Weighted Average:** Precision = 0.96, Recall = 0.95, F1-Score = 0.95  

### 📊 Confusion Matrix

Each row represents the **true label**, and each column represents the **predicted label**.

|                        | Predicted: Correct | Predicted: Partially Correct | Predicted: Incorrect |
|------------------------|-------------------:|-----------------------------:|----------------------:|
| **Actual: Correct**            | 12,719              | 340                         | 473                   |
| **Actual: Partially Correct** | 99                  | 113                         | 108                   |
| **Actual: Incorrect**         | 317                 | 262                         | 16,035                |

**Interpretation:**
- **Diagonal values** indicate correct predictions per class.
- **Off-diagonal values** are misclassifications.

### Notes

- The model demonstrates strong performance for the **"Correct"** and **"Incorrect"** categories.
- The **"Partially Correct"** class, which has fewer samples, shows lower recall (35%) and F1-score (22%).
- These metrics highlight an area for potential improvement, such as:
  - Gathering more balanced training examples
  - Refining label definitions
  - Considering model-specific tuning or loss reweighting

---

## ⚙️ Training Details

- **Batch Size**: 1  
- **Gradient Accumulation Steps**: 8  
- **Max Seq Length**: 512  
- **LoRA Rank**: 64  
- **Learning Rate**: 2e-4  
- **Epochs**: 5 
- **Trainer**: `SFTTrainer` from Hugging Face TRL

---

## 📌 Acknowledgments

- Fine-tuning powered by [PEFT](https://github.com/huggingface/peft) + [QLoRA](https://arxiv.org/abs/2305.14314)  
- Logging with [Weights & Biases](https://wandb.ai)  
- Base model by Meta AI
