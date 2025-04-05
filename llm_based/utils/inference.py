from langchain.prompts import ChatPromptTemplate

def get_chain(model, template):
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model

def run_single_prediction(chain, prompt_context, question, response, correct_answer):
    return chain.invoke({
        "prompt_context": prompt_context,
        "question": question,
        "student_response": response,
        "correct_answer": correct_answer
    })