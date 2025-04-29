import pandas as pd
import os
import json

from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate

from prompts.template import TEMPLATE
from prompts.few_shot import create_few_shot_examples, few_shot_format

# Load the config file
with open('../config/config.json', 'r') as f:
    config = json.load(f)

# Load data
df_train = pd.read_csv(os.path.join(config["data_loc"], "train.csv"), encoding='windows-1252')
df_test = pd.read_csv(os.path.join(config["data_loc"], "test.csv"), encoding='windows-1252')

# Create few-shot examples
few_shot_df = create_few_shot_examples(df_train, n=2)
prompt_context = "\n".join(few_shot_df.apply(few_shot_format, axis=1).tolist())

# Initialize the model
model = OllamaLLM(model="llama3.2")

# Define the prompt template
prompt = ChatPromptTemplate.from_template(TEMPLATE)

# Create the chain
chain = prompt | model 

# Run one example
row = df_test.iloc[1]
result = chain.invoke({
        "prompt_context": prompt_context,
        "question": row["Question"],
        "student_response": row["Response"],
        "correct_answer": row["CorrectAnswer"]
        })

# Output
formatted_prompt = prompt.format_messages(
    prompt_context=prompt_context,
    question=row["Question"],
    student_response=row["Response"],
    correct_answer=row["CorrectAnswer"]
)
print("=== Prompt Sent ===\n", formatted_prompt[0].content, "\n")

print("=== Result ===\n", result)