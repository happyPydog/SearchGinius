from pathlib import Path
from typing import Iterable, Iterator, List


def list_all_files(directory: str) -> Iterator[Path]:
    """Yield all files from the given directory."""
    return Path(directory).rglob("*")


def filter_files_by_type(
    files: Iterator[Path], file_types: Iterable[str]
) -> Iterable[Path]:
    """Filter files by the given file types."""
    return (file for file in files if file.suffix in file_types)


def get_file_paths(directory: str, file_types: List[str]) -> List[Path]:
    """Get file paths from the specified directory, filtered by the provided file types."""
    return list(filter_files_by_type(list_all_files(directory), file_types))
