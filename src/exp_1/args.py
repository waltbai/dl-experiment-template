"""Arguments in each phase."""

from dataclasses import dataclass
from transformers import Seq2SeqTrainingArguments

from llama_factory.llmtuner.hparams import (
    DataArguments,
    ModelArguments,
    FinetuningArguments,
)

@dataclass
class PrepareArguments(DataArguments):
    """Arguments for prepare phase."""
    prepare_dir: str = ""


@dataclass
class TrainingArguments(Seq2SeqTrainingArguments):
    """Arguments for training phase."""


def postprocess_args(
    data_args: DataArguments,
    model_args: ModelArguments,
    training_args: Seq2SeqTrainingArguments,
    finetuning_args: FinetuningArguments,
):
    """Postprocess arguments, modified from llama-factory."""
