from lxml import etree
from pathlib import Path
from typing import Optional

from .errors import InvalidSVGError


def render(input_code: str, input_path: Optional[Path] = None) -> bytes:
	"""Render SVG code into PNG binary data

	Args:
		input_code (str): SVG code
		input_path (Optional[Path]): input SVG's path (for error messages)

	Returns:
		bytes: PNG binary data

	Raises:
		InvalidSVGError: invalid SVG code
	"""

	validate(input_code, input_path=input_path)

def validate(input_code: str, input_path: Optional[Path] = None) -> None:
	"""Validate given SVG code

	Args:
		input_code (str): SVG code
		input_path (Optional[Path]): input SVG's path (for error messages)

	Raises:
		InvalidSVGError: invalid SVG code
	"""

	raise NotImplementedError