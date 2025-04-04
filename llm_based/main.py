from langchain_ollama.llms import OllamaLLM
from langchain.prompts.chat import ChatPromptTemplate

# Initialize the model
model = OllamaLLM(model="llama3.2")

# Create a prompt template
template = """"
You are a professor and you are grading short answer questions.

You will be given a question, a student response, and the correct answer.

The goal is to grade the student response based on the correct answer.

The answers should be labeled as 1, 0, or -1.
Label 1 means the student response is correct.
Label 0 means the response is similar to the correct answer but not precise.
Label -1 means the response is incorrect.

Here are some examples of grading:
Question: {question}
Student Response: {student_response}
Correct Answer: {correct_answer}
Label:
"""

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    template=template
)

# Create a chain
chain = prompt | model

# Define the inputs
result = chain.invoke(
    {
        "question": "What is the capital of France?",
        "student_response": "Paris is the capital of France.",
        "correct_answer": "The capital of France is Paris.",
        "label": []
    }
)

# Print the result c
print(result)