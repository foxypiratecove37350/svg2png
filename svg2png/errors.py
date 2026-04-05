from pathlib import Path
from typing import NoReturn

class InvalidSVGError(Exception):
	def __init__(self, input_code: str) -> NoReturn:
		super().__init__(f"Invalid SVG: {input_code}")