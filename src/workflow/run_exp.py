"""It is recommended to create an individual file for each model variant."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class ExperimentArguments:
	"""Arguments for running experiment."""
	stage: Literal["prepare", "train", "evaluate", "test"] = "prepare"


if __name__ == "__main__":
	pass
