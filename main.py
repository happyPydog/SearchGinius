"""Entry point."""
import argparse

from langchain import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from rich import print

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def main(query: str):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    db = FAISS.load_local(
        folder_path="vector_store", embeddings=embeddings, index_name="index"
    )
    docs = db.similarity_search(query)
    print(docs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Searching for local files.")
    parser.add_argument("query", type=str, help="Query to search in the database.")

    args = parser.parse_args()
    main(args.query)
