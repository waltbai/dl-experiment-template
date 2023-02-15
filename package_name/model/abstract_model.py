"""Abstract model."""
import logging
import os
from abc import ABC
from typing import Callable, Any

import torch
from torch import nn
from yacs.config import CfgNode

from package_name.util.config import load_config, save_config


__all__ = ["AbstractModel"]


def _predict_unimplemented(self, *inputs: Any) -> None:
    """Define the predict method in production environment.

    The predict method receives raw data, preprocesses them,
        forwards the processed data, obtains output and
        finally translates the output to annotations/labels.
        In this situation, a light processor may be needed.
    """
    raise NotImplementedError


class AbstractModel(nn.Module):
    """Abstract model class."""

    def __init__(self,
                 config: CfgNode = None,
                 device: str = "cpu",
                 default_config: CfgNode = None,
                 **kwargs):
        """Construction method of BasicPredictor class.

        Args:
            config (dict): configuration.
            device (str, optional): device name.
                Defaults to "cpu".
        """
        super(AbstractModel, self).__init__()
        # Merge model specific default config
        if default_config is None:
            default_config = config
        else:
            default_config.merge_from_other_cfg(config)
        self.config = default_config
        # System configuration
        self.log = self.config.SYSTEM.log
        self.device = device
        # Model configuration
        self.name = self.config.MODEL.name
        self.backbone = self.config.MODEL.backbone
        # Components
        self.logger = logging.getLogger(f"{self.backbone}.{self.name}")

    # Only need to be implemented in Prediction Environment
    predict: Callable[..., Any] = _predict_unimplemented

    @classmethod
    def from_checkpoint(cls, checkpoint: str, device: str = "cpu"):
        """Load model from checkpoint.

        Two files should be in the checkpoint directory:
            ``config.yml`` and ``model.pt``
        """
        # Load config file
        config_path = os.path.join(checkpoint, "config.yml")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Cannot find {config_path}!")
        config = load_config(config_path)
        # Build model by config
        model = cls(config, device)
        # Load model parameters
        model_path = os.path.join(checkpoint, "model.pt")
        if not os.path.exists(model_path):
            model.logger.warning(
                f"Fail to load model parameters from {model_path}! "
                f"Use randomly initialized parameters."
            )
        else:
            model_params = torch.load(model_path, map_location=device)
            model.load_state_dict(model_params)
        # Load preprocess data
        model.load_preprocess_data(checkpoint)
        # Switch device
        model = model.to(device)
        return model

    def save_checkpoint(self, checkpoint: str):
        """Save model to checkpoint."""
        if not os.path.exists(checkpoint):
            os.makedirs(checkpoint)
        # Save config file
        config_path = os.path.join(checkpoint, "config.yml")
        save_config(self.config, config_path)
        # Save model parameters
        model_path = os.path.join(checkpoint, "model.pt")
        model_params = self.cpu().state_dict()
        if os.path.exists(model_path):
            pass
        torch.save(model_params, model_path)
        # Save preprocess data
        self.save_preprocess_data(checkpoint)
