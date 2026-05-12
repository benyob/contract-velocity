from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT = """
You are assisting an internal legal review workflow.

You are NOT a final legal authority.

Given:
- extracted clauses
- detected deviations
- historical precedents

Your tasks:
1. Summarize potential risk
2. Identify unusual changes
3. Suggest likely handling
4. Recommend escalation if needed
5. Provide confidence score
"""


def analyze_contract(text, clauses, deviations, precedents):

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": f"""
                Clauses: {clauses}

                Deviations: {deviations}

                Historical precedents: {precedents}
                """
            }
        ]
    )

    return completion.choices[0].message.content