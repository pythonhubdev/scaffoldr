from enum import Enum


class StatusEnum(str, Enum):
	SUCCESS = "success"
	ERROR = "error"
	FAILURE = "failure"
