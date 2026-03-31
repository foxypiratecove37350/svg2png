from pathlib import Path
from typing import NoReturn

class InvalidSVGError(Exception):
	def __init__(self, path_or_content: str | Path) -> NoReturn:
		super(f"Invalid SVG: {path_or_content}")