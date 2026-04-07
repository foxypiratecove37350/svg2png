from pathlib import Path
from typing import Optional

class InvalidSVGError(Exception):
	def __init__(self, input_code: str, input_path: Optional[Path] = None) -> None:
		super().__init__(f'Invalid SVG "{input_code}"{f" in \"{input_path}\"" if input_path else ""}')