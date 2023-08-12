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
