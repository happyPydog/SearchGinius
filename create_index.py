"""Create the index for project."""
import ast

from langchain.embeddings import OpenAIEmbeddings
from rich import print

from file import get_file_paths

PROJET_DIR = "./MetaGPT/metagpt"
SUPPORTED_FILE_TYPES = [".py"]


def main():
    file_paths = get_file_paths(PROJET_DIR, SUPPORTED_FILE_TYPES)

    for path in file_paths:
        ...


if __name__ == "__main__":
    main()
