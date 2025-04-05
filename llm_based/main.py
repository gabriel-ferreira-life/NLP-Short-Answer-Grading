from langchain_ollama.llms import OllamaLLM
from langchain.prompts.chat import ChatPromptTemplate
from few_show_format import few_shot_format, create_few_shot_examples
import pandas as pd
import os
import json


# Load the config file
with open('../config/config.json', 'r') as f:
    config = json.load(f)

# Data location
file_path = config["data_loc"]

# Load the train dataset
final_path = os.path.join(file_path, "train.csv") 
df_train = pd.read_csv(final_path, encoding='windows-1252')

# Load the test dataset
final_path = os.path.join(file_path, "test.csv") 
df_test = pd.read_csv(final_path, encoding='windows-1252')

# Initialize the model
model = OllamaLLM(model="llama3.2")

# Create a prompt template
template = """
You are a professor grading short answer questions.

You will be given a question, a student response, and the correct answer.

Your job is to assign a label:
- 1 if the response is correct
- 0 if the response is somewhat correct but not precise
- -1 if the response is incorrect

Below are some graded examples:
{prompt_context}

Now grade this new response:
Question: {question}
Student Response: {student_response}
Correct Answer: {correct_answer}

Respond with only the label number: 1, 0, or -1. Do not explain.
Label:
"""

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    template=template
)

# Create a chain
chain = prompt | model

# Create few-shot examples
few_shot_df = create_few_shot_examples(df_train, n=1)
prompt_context = "\n".join(few_shot_df.apply(few_shot_format, axis=1).tolist())

# Define the inputs
result = chain.invoke(
    {
        "prompt_context": f"{prompt_context}",
        "question": df_test.iloc[0]["Question"],
        "student_response": df_test.iloc[0]["Response"],
        "correct_answer": df_test.iloc[0]["CorrectAnswer"],
        "Label": []
    }
)

# Print the prompt context
formatted_prompt = prompt.format_messages(
    prompt_context=prompt_context,
    question=df_test.iloc[0]["Question"],
    student_response=df_test.iloc[0]["Response"],
    correct_answer=df_test.iloc[0]["CorrectAnswer"],
)
print("=== Final Prompt Sent to LLM ===")
print(formatted_prompt[0].content, "\n")

# Print the result
print("=== Result ===")
print(result, "\n")