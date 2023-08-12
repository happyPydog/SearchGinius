"""Summary the source code based on LLMs."""
from typing import cast

import openai

from schema import ChatGPTResponse


def summary_code(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a smart Python programmer."},
            {
                "role": "user",
                "content": f"Given a source code in triple backticks, use at most 3 sentences to summarize it.\n\n```python\n{text}\n```"
            },
        ],
    )
    response = cast(ChatGPTResponse, response)

    return response["choices"][0]["message"]["content"]


def tag_code(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a smart Python programmer."},
            {
                "role": "user",
                "content": f"Given the source code enclosed in triple backticks, please provide a brief descriptive tag or phrase for the code. This tag will be used for similarity search to locate relevant source code based on the provided text.\nHere's the source code: ```python\n{text}\n```"
            },
        ],
        temperature=0.7,
    )
    response = cast(ChatGPTResponse, response)

    return response["choices"][0]["message"]["content"]
