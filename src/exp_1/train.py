from dataclasses import dataclass
import logging

from datasets import Dataset
from torch import nn

from .args import TrainingArguments


logger = logging.getLogger(__name__)



def get_model_name(
		training_args: TrainingArguments,
		**kwargs,
):
	"""Generate model name from training arguments."""


def train(
		model: nn.Module,
		train_set: Dataset,
		valid_set: Dataset,
		training_args: TrainingArguments,
		**kwargs,
):
	"""Train on train and valid sets."""
