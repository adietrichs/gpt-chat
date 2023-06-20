import tiktoken

from classes import *


TOKEN_PARAMS = {
    ModelFamily.GPT_3: {"per_message": 5},
    ModelFamily.GPT_4: {"per_message": 4},
}


def calculate_prompt_tokens(messages: list[Message], model: Model) -> int:
    embedding = tiktoken.encoding_for_model(str(model))
    return 3 + sum(
        len(embedding.encode(message.content))
        + TOKEN_PARAMS[model.family]["per_message"]
        for message in messages
    )


def calculate_completion_tokens(choices: list[Choice], model: Model) -> int:
    embedding = tiktoken.encoding_for_model(str(model))
    return sum(len(embedding.encode(choice.message.content)) for choice in choices)
