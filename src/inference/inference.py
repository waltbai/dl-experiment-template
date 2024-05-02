from datasets import Dataset
from torch import nn

from src.train.train import TrainingArguments, get_model_name


def evaluate(
        model: nn.Module,
        eval_set: Dataset,
        training_args: TrainingArguments,
        **kwargs,
):
    """Evaluate on eval dataset."""
