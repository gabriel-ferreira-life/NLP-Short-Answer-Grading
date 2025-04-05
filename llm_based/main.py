import pandas as pd
import os
import json

from langchain_ollama.llms import OllamaLLM

from prompts.template import TEMPLATE
from utils.few_shot import create_few_shot_examples, few_shot_format
from utils.inference import get_chain, run_single_prediction

# Load the config file
with open('../config/config.json', 'r') as f:
    config = json.load(f)

# Load data
df_train = pd.read_csv(os.path.join(config["data_loc"], "train.csv"), encoding='windows-1252')
df_test = pd.read_csv(os.path.join(config["data_loc"], "test.csv"), encoding='windows-1252')

# Create few-shot examples
few_shot_df = create_few_shot_examples(df_train, n=1)
prompt_context = "\n".join(few_shot_df.apply(few_shot_format, axis=1).tolist())

# Initialize the model
model = OllamaLLM(model="llama3.2")
chain = get_chain(model, TEMPLATE)

# Run one example
row = df_test.iloc[1]
result = run_single_prediction(
    chain,
    prompt_context,
    row["Question"],
    row["Response"],
    row["CorrectAnswer"]
)

# Output
print("=== Prompt Sent ===\n", chain.prompt.format_messages(
    prompt_context=prompt_context,
    question=row["Question"],
    student_response=row["Response"],
    correct_answer=row["CorrectAnswer"]
)[0].content, "\n")

print("=== Result ===\n", result)