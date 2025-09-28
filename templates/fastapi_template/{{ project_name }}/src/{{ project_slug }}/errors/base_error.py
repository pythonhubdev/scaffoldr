from http import HTTPStatus


class BaseError(Exception):
	"""
	Base exception class for the application.
	"""

	def __init__(
		self,
		message: str,
		status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR,
	) -> None:
		"""
		Initializes the BaseError.

		Args:
			message: The error message.
			status_code: The HTTP status code.

		"""
		self.message: str = message
		self.status_code: int = status_code
		super().__init__(message)
