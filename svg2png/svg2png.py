""""
Render an SVG file into a PNG file
"""

from typing import Optional
from pathlib import Path
from warnings import deprecated

from .renderer import render

@deprecated("Use specialized functions instead.")
def svg2png(input: str | Path) -> Optional[bytes]:
	"""Render SVG into PNG

	Args:
		input (str | Path): input SVG's path or SVG code

	Returns:
		Optional[bytes]: PNG data
	"""

	raise NotImplementedError

def svg_path2png_path(input_path: Path, output_path: Optional[Path]) -> None:
	"""Render SVG file into PNG file

	Args:
		input_path (Path): input SVG's path
		output_path (Optional[Path]): output PNG's path

	Raises:
		FileNotFoundError: input SVG file not found
	"""

	if not input_path.exists() or not input_path.is_file():
		raise FileNotFoundError(input_path)
	if not output_path:
		output_path = input_path.with_suffix('.png')

	with open(input_path, 'r') as input_file:
		input_code = input_file.read()
	
	svg_code2png_path(input_code, output_path)

def svg_path2png_bin(input_path: Path) -> bytes:
	"""Render SVG file and return PNG as bytes

	Args:
		input_path (Path): input SVG's path

	Returns:
		bytes: PNG data
	"""
	
	with open(input_path, 'r') as input_file:
		input_code = input_file.read()
	
	return svg_code2png_bin(input_code)


def svg_code2png_path(input_code: str, output_path: Path) -> None:
	"""Render provided SVG code into a PNG file

	Args:
		input_code (str): SVG code
		output_path (Path): output PNG's path
	"""
	
	with open(output_path, 'wb') as output_file:
		output_file.write(svg_code2png_bin(input_code))

def svg_code2png_bin(input_code: str) -> bytes:
	"""Render provided SVG code and return PNG as bytes

	Args:
		input_code (str): SVG code

	Returns:
		bytes: PNG data
	"""

	return render(input_code)