from importlib.util import find_spec
from pathlib import Path


class Helper:
	@staticmethod
	def module_to_os_path(dotted_path: str = "app") -> Path:
		"""
		Find Module to OS Path.

		Return a path to the base directory of the project or the module
		specified by `dotted_path`.

		Args:
		----
			dotted_path: The path to the module. Defaults to "app".

		Raises:
		------
			TypeError: The module could not be found.

		Returns:
		-------
			Path: The path to the module.

		"""
		try:
			if (src := find_spec(dotted_path)) is None:  # pragma: no cover
				type_error = f"Couldn't find the path for {dotted_path}"
				raise TypeError(type_error)
		except ModuleNotFoundError as e:
			type_error = f"Couldn't find the path for {dotted_path}"
			raise TypeError(type_error) from e

		path = Path(str(src.origin))
		return path.parent if path.is_file() else path
