from pydantic import BaseModel


class FileInfo(BaseModel):
	"""File information model."""

	key: str
	size: int
	last_modified: str
	etag: str
	content_type: str | None = None


class UploadResult(BaseModel):
	"""Upload result model."""

	key: str
	etag: str
	version_id: str | None = None
