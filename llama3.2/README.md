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

Evaluation was conducted using prompt-based generation and label matching. The output was compared against gold labels using macro F1, accuracy, precision, and recall.
<!-- 
---

## ⚙️ Training Details

- **Batch Size**: 1  
- **Gradient Accumulation Steps**: 8  
- **Max Seq Length**: 512  
- **LoRA Rank**: 64  
- **Learning Rate**: 2e-4  
- **Epochs**: 1  
- **Trainer**: `SFTTrainer` from Hugging Face TRL -->

---

## 📌 Acknowledgments

- Fine-tuning powered by [PEFT](https://github.com/huggingface/peft) + [QLoRA](https://arxiv.org/abs/2305.14314)  
- Logging with [Weights & Biases](https://wandb.ai)  
- Base model by Meta AI
