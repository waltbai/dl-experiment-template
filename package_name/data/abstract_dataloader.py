"""Abstract dataloader."""
import random
from abc import ABC, abstractmethod

from package_name.data.abstract_dataset import AbstractDataset
from package_name.data.dataset_list import DatasetList


class AbstractDataLoader(ABC):
    """Basic data loader.

    Currently, it does not support multiprocessing.
    """

    def __init__(self,
                 dataset: AbstractDataset or DatasetList,
                 batch_size: int = 1,
                 shuffle: bool = False):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __iter__(self):
        if isinstance(self.dataset, DatasetList):
            for dataset in self.dataset:
                yield self.yield_dataset(dataset)
        else:
            yield self.yield_dataset(self.dataset)

    def yield_dataset(self, dataset: AbstractDataset):
        """Yield a dataset."""
        num_data = len(dataset)
        indices = list(range(num_data))
        if self.shuffle:
            random.shuffle(indices)
        for start in range(0, num_data, self.batch_size):
            end = start + self.batch_size
            yield self.make_batch(dataset, indices[start:end])

    @abstractmethod
    def make_batch(self,
                   dataset: AbstractDataset,
                   indices: list):
        """Make batch for """
        pass
