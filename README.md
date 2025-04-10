# NLP-Short-Answer-Grading
This project fine-tunes the LLaMA 3.2-3B Instruct model to grade short-answer responses in educational settings. The model classifies student answers into three categories: Correct, Partially Correct, or Incorrect.

```text
NLP-Short-Answer-Grading/
├── config/
│ ├── config.json # Configuration file with data paths
│ └── requirements.txt # Python dependencies
│
├── data/
│ ├── train.csv # Training dataset
│ └── test.csv # Test dataset
│
├── exploration/
│ └── eda.ipynb # Exploratory Data Analysis
│
├── few_shot_exploration/
│ ├── main.py # Entry point: loads data, formats prompt, runs predictions
│ └── prompts/
│  ├── few_shot.py # Functions to format few-shot examples
│  └── template.py # Prompt template used by the LLM
│
├── llama3.2/
│ ├── nlp-short-answer-grading-llama-fine-tunning.ipynb
│ └── nlp-short-answer-grading-llama-inference.ipynb
│
└── problem_description/
  └── Final project.pdf # Project Description

```
