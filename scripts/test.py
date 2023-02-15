"""Test scripts."""
import logging
from argparse import ArgumentParser

from package_name.util.config import load_config, update_config_via_cmd


def parse_args():
    """Parse commandline arguments."""
    parser = ArgumentParser("package_name.train")
    parser.add_argument("--config", default="config/default.yml",
                        help="config file path")
    parser.add_argument("--device", default="cpu",
                        help="device")
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    args = parse_args()
    config = load_config(args.config)
    update_config_via_cmd(config, args)
    # model.validate()
    # model.test()
