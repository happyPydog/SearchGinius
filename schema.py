"""Common schema."""
from enum import Enum
from typing import Dict, List, TypedDict


class SupportedFileTypes(str, Enum):
    PYTHON = ".py"


class SourceCodeData(TypedDict):
    modules: List[str]
    functions_called: List[str]
    global_vars: List[str]
    classes_used: List[str]
    function_codes: Dict[str, str]
    class_codes: Dict[str, str]


## OPENAI CHAT COMPLETION RESPONSE TYPE ##
class ChoiceMessage(TypedDict):
    role: str
    content: str


class Choice(TypedDict):
    index: int
    message: ChoiceMessage
    finish_reason: str


class Usage(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatGPTResponse(TypedDict):
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: Usage
