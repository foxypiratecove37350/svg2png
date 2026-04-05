from lxml import etree

from .errors import InvalidSVGError

def render(input_code: str) -> bytes:
	"""Render SVG code into PNG binary data

	Args:
		input_code (str): SVG code

	Returns:
		bytes: PNG binary data

	Raises:
		InvalidSVGError: invalid SVG code
	"""

	raise InvalidSVGError(input_code)