"""It is recommended to create an individual file for each prepare settings."""


from dataclasses import dataclass


__all__ = [
	"PrepareArguments",
	"prepare"
]


@dataclass
class PrepareArguments:
	"""Arguments for prepare stage."""
	dataset_dir: str = "data"
	dataset: str = ""
	prepare_dir: str = ""


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
