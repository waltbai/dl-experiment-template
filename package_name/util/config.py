"""Config."""
from argparse import Namespace

from yacs.config import CfgNode


def load_config(config_path: str = None) -> CfgNode:
    """Load config from path.

    This function will automatically load
        default configs from ``config/default.yml``.
        If ``config_path`` is not None, it will
        overwrite the default config.
    """
    with open("config/default.yml", "r") as f:
        config = CfgNode.load_cfg(f)
    config.set_new_allowed(True)
    if config_path is not None:
        config.merge_from_file(config_path)
    return config


def save_config(config: CfgNode, config_path: str) -> None:
    """Save config to path."""
    with open(config_path, "w") as f:
        f.write(config.dump())


def update_config_via_cmd(config: CfgNode, args: Namespace):
    """Update config via command line.

    Currently, we only update device information.
    """
    config.SYSTEM.device = args.device

