# Automated Short Answer Grading (NLP 579 Final Project)

This repository presents a comparative study of three approaches to automatically grade short student responses using NLP models. We evaluate performance across a dataset of science-domain questions labeled as **Correct**, **Partially Correct**, or **Incorrect**.

## ⚙️ Repo Structure

```text
NLP-Short-Answer-Grading/
├── config/
│  ├── config.json           # Configuration file with data paths
│  └── requirements.txt      # Python dependencies
│
├── data/
│  ├── train.csv             # Training dataset
│  └── test.csv              # Test dataset
│
├── problem_description/    # Project Description
│
├── exploration/            # Jupyter Notebooks
│  └── eda.ipynb             # Exploratory Data Analysis
│
├── solutions\
│  └── few_shot_exploration/
│    ├── main.py               # Entry point: loads data, formats prompt, runs predictions
│    └── prompts/
│      ├── few_shot.py          # Functions to format few-shot examples
│      └── template.py          # Prompt template used by the LLM
│  └── llama3.2/
│    ├── nlp-short-answer-grading-llama-fine-tunning.ipynb
│    └── nlp-short-answer-grading-llama-inference.ipynb
│  └── bert/
│    ├── BERT_Based_Model.ipynb
│    └── bert_based_model.py
│  └── rule_based/
│    └── Rule_Based_Model.ipynb
│
└── Report/                 # Project Report

```


## 🧠 Models Compared

### 1. Rule-Based Heuristic
- Uses keyword overlap between reference and student response.
- Simple and interpretable, but brittle to paraphrasing.

---

### 2. RoBERTa (BERT-based Classifier)
- Fine-tuned on concatenated input: `[CLS] Question [SEP] Reference Answer [SEP] Student Response`.
- Strong performance on "Correct" and "Incorrect", struggled with "Partially Correct".

---

### 3. LLaMA-3B (LLM-based Classifier)
- Instruction-tuned using LoRA adapters.
- Highest accuracy and the only model to capture partial correctness meaningfully.

## 📊 Results Summary

| Model        | Accuracy | Macro-F1 | Weighted-F1 |
|--------------|----------|----------|--------------|
| Rule-Based   | 70.0%    | 48.0%    | 71.0%        |
| RoBERTa      | 91.7%    | 61.0%    | 91.0%        |
| LLaMA-3B     | 94.8%    | 71.0%    | 95.0%        |

See heatmaps in the `images/` folder for a per-class breakdown.

---

## 📁 Dataset

- 30,000+ labeled student responses
- Classes:
  - **2** = Correct
  - **1** = Partially Correct
  - **0** = Incorrect
- Notably imbalanced (only ~1% are Partially Correct)

Note: Data is hidden for privacy purposes.
---

## Report & Analysis
For a detailed report on findings and term analysis, refer to:
[Phrase Mining Report (PDF)](report/COMS_5790_Final_Project_Report.pdf). 

--

## 📄 Authors

Nicholas George \
Gabriel Ferreira \
Bhavika Gungurthi
