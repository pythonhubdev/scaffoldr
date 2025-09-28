from typing import TYPE_CHECKING, cast

import typer
from copier import subprocess

from scaffoldr.core.constants.const import CloudTypes

if TYPE_CHECKING:
	from collections.abc import Iterable


class Helper:
	@staticmethod
	def post_hook(path: str) -> None:
		"""
		Run post-generation hooks in the given `path`.

		The function executes the commands in sequence inside the target directory.
		Raises subprocess.CalledProcessError if any command fails.
		"""
		commands: Iterable[list[str]] = [
			["uv", "sync", "--quiet"],
			["uv", "run", "ruff", "format", ".", "--silent"],
			["uv", "run", "ruff", "check", ".", "--unsafe-fixes", "--silent"],
		]

		for cmd in commands:
			try:
				# use cwd instead of a separate "cd" process so the child runs in `path`
				subprocess.run(cmd, check=True, cwd=path)
			except subprocess.CalledProcessError as exc:
				raise RuntimeError(f"Command `{cmd}` failed in {path}") from exc

	@staticmethod
	def cloud_type() -> str:
		"""
		Detect the cloud environment type based on environment variables.
		"""
		cloud_types = list(CloudTypes)
		cloud_type: str = cast("str", typer.prompt(f"Cloud type: {' | '.join(cloud_types)}"))
		if cloud_type in cloud_types:
			return cloud_type
		raise ValueError(
			f"Invalid cloud type: {cloud_type}. Must be one of: {' | '.join(cloud_types)}",
		)
