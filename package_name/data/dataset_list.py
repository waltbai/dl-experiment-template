"""Dataset list class."""
import os
from typing import Type

from package_name.data.abstract_dataset import AbstractDataset


class DatasetList:
    """Sliced datasets.

    This object will load datasets from specified directory one-by-one.
    Each dataset type is required.
    """

    def __init__(self,
                 dataset_dir: str,
                 dataset_class: Type[AbstractDataset] = AbstractDataset,
                 **kwargs):
        super(DatasetList, self).__init__(**kwargs)
        self.dataset_dir = dataset_dir
        self.dataset_class = dataset_class

    def __iter__(self):
        for fn in os.listdir(self.dataset_dir):
            fp = os.path.join(self.dataset_dir, fn)
            yield self.dataset_class.from_file(fp)
