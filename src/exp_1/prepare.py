"""It is recommended to create an individual file for each prepare settings."""

import logging

from .args import PrepareArguments


__all__ = [
	"get_data_name",
	"prepare"
]


logger = logging.getLogger(__name__)


def get_data_name(
		prepare_args: PrepareArguments,
		**kwargs,
) -> str:
	"""Generate data file name via arguments."""


def prepare(
		args: PrepareArguments,
		**kwargs,
):
	"""Main prepare function."""
