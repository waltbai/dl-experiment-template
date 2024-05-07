"""It is recommended to create an individual folder for each model variant."""

from dataclasses import dataclass
import logging

from .args import PrepareArguments, TrainingArguments


logger = logging.getLogger(__name__)


@dataclass
class ModelArguments:
    """Arguments for model."""
    model_name_or_path: str


ARGS = (
    PrepareArguments,
    ModelArguments,
    TrainingArguments,
)


if __name__ == "__main__":
	pass
