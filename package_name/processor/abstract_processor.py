"""Abstract processor."""
from abc import ABC, abstractmethod

from yacs.config import CfgNode


class AbstractProcessor(ABC):
    """Abstract processor.

    Basically, three methods are required: construct_[train/dev/test]_set.
    These three sets can be directly load by a Dataset or DatasetList class.
    The dataset path is given. If any other steps are needed, override
    ``preprocess`` method. It will be called before the above three methods.
    """

    def __init__(self,
                 config: CfgNode = None,
                 default_config: CfgNode = None,
                 **kwargs):
        # Merge model specific default config
        if default_config is None:
            default_config = config
        else:
            default_config.merge_from_other_cfg(config)
        self.config = default_config
        self.name = self.config.PROCESSOR.name
        # System settings
        self.disable_tqdm = not self.config.SYSTEM.tqdm
        self.log = self.config.SYSTEM.log
        self.data_dir = self.config.SYSTEM.data_dir      # Raw data directory
        self.work_dir = self.config.SYSTEM.work_dir      # Intermediate data directory
        # Log
        self.logger = None

    def preprocess(self):
        """Anything to be done before construct_[train/dev/test]_set."""
        pass

    @abstractmethod
    def construct_train_set(self, train_set_path: str):
        """Construct train set."""

    @abstractmethod
    def construct_dev_set(self, dev_set_path: str):
        """Construct dev set."""

    @abstractmethod
    def construct_test_set(self, test_set_path: str):
        """Construct test set."""
