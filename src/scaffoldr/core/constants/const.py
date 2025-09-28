from enum import Enum

from rich.console import Console

console = Console()


class Frameworks(str, Enum):
	FASTAPI = "fastapi"
	LITESTAR = "litestar"
	FLASK = "flask"
	QUARTZ = "quartz"
	ROBYN = "robyn"


class CloudTypes(str, Enum):
	AWS = "aws"
	GCP = "gcp"
	AZURE = "azure"
	NONE = "none"


class DatabaseTypes(str, Enum):
	SQLALCHEMY = "sqlalchemy"
	MONGODB = "mongodb"
