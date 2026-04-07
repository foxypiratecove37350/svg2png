from lxml import etree
from pathlib import Path
from typing import Optional

from .errors import InvalidSVGError


def render(input_code: str, input_path: Optional[Path] = None) -> bytes:
	"""Render SVG code into PNG binary data

	Args:
		input_code (str): SVG code

	Returns:
		bytes: PNG binary data

	Raises:
		InvalidSVGError: invalid SVG code
	"""

	raise InvalidSVGError(input_code, input_path)