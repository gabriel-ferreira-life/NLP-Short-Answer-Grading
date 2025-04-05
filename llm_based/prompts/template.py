TEMPLATE = """
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