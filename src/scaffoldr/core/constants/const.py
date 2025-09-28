from enum import Enum

from rich.console import Console

console = Console()


class Frameworks(str, Enum):
	FASTAPI = "fastapi"
	LITESTAR = "litestar"
	FLASK = "flask"
	QUARTZ = "quartz"
	ROBYN = "robyn"
