"""Abstract dataset."""
from abc import ABC, abstractmethod


class AbstractDataset(ABC):
    """Abstract dataset."""

    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass

    @classmethod
    @abstractmethod
    def from_file(cls, file_path: str):
        """Load dataset from file."""

