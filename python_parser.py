"""Parser for Python source files."""
import ast
from typing import List, Optional, Type, Union

from schema import SourceCodeData


class ImportExtractor:
    @staticmethod
    def extract(node: ast.AST) -> List[str]:
        if isinstance(node, ast.Import):
            return [n.name for n in node.names]
        elif isinstance(node, ast.ImportFrom):
            return [f"{node.module}.{n.name}" for n in node.names]
        return []


class FunctionCallExtractor:
    @staticmethod
    def extract(node: ast.AST) -> List[str]:
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                return [node.func.id]
            elif isinstance(node.func, ast.Attribute):
                return [node.func.attr]
        return []


class GlobalVarExtractor:
    @staticmethod
    def extract(node: ast.AST) -> List[str]:
        return node.names if isinstance(node, ast.Global) else []


class ClassUsageExtractor:
    @staticmethod
    def extract(node: ast.AST) -> List[str]:
        return [node.name] if isinstance(node, ast.ClassDef) else []


def extract_code_segment(
    code: str, node: Union[ast.FunctionDef, ast.ClassDef]
) -> Optional[str]:
    # Use the line numbers provided by the ast node
    start_line = node.lineno - 1  # AST line numbers are 1-based, lists are 0-based
    end_line = node.end_lineno if hasattr(node, "end_lineno") else start_line
    return "\n".join(code.splitlines()[start_line : end_line + 1])


def extract_from_node(extractor: Type, node: ast.AST) -> List[str]:
    return extractor.extract(node)


def analyze_code(code: str) -> SourceCodeData:
    tree = ast.parse(code)

    data: SourceCodeData = {
        "modules": [],
        "functions_called": [],
        "global_vars": [],
        "classes_used": [],
        "function_codes": {},
        "class_codes": {},
    }

    extractors = {
        "modules": ImportExtractor,
        "functions_called": FunctionCallExtractor,
        "global_vars": GlobalVarExtractor,
        "classes_used": ClassUsageExtractor,
    }

    for key, extractor in extractors.items():
        for node in ast.walk(tree):
            data[key].extend(extract_from_node(extractor, node))

    for node in tree.body:  # Only top-level nodes
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            data["function_codes"][node.name] = extract_code_segment(code, node)
        elif isinstance(node, ast.ClassDef):
            data["class_codes"][node.name] = extract_code_segment(code, node)

    return data
