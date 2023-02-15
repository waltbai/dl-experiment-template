"""Default trainer.

If the model is only used in experiments,
we just need a trainer to control the process
steps.
"""
from yacs.config import CfgNode

from package_name import CLASSES


class DefaultTrainer:
    """Default trainer."""

    def __init__(self,
                 config: CfgNode,
                 device: str = "cpu",
                 **kwargs):
        # Settings
        self.processor_name = config.PROCESSOR.name
        self.model_backbone = config.MODEL.backbone
        self.dataset_type = config.MODEL.dataset
        self.optimizer_name = config.TRAIN.optimizer.name
        self.skip_process = config.TRAIN.skip_process
        self.skip_train = config.TRAIN.skip_train
        self.skip_test = config.TRAIN.skip_test
        self.device = device
        # Components
        self.processor = CLASSES.get(f"processor.{self.processor_name}")(config)
        self.model = CLASSES.get(f"model.{self.model_backbone}")(config, device)
        self.dataset_class = CLASSES.get(f"dataset.{self.dataset_type}")
        self.optimizer = None
        self.scheduler = None

    def run(self):
        """Main process."""
        # Process raw data
        if not self.skip_process:
            self.processor.preprocess()
            self.processor.construct_train_set()
            self.processor.construct_dev_set()
            self.processor.construct_test_set()
        # Build dataset
        # Train and valid
        if not self.skip_train:
            self.train()
        # Test
        if not self.skip_test:
            self.test()

    def train(self):
        pass

    def valid(self):
        pass

    def test(self):
        pass
