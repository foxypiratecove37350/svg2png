"""
Render an SVG file into a PNG file
"""

from typing import Optional
from pathlib import Path
from warnings import deprecated

from .renderer import render

@deprecated("Use specialized functions instead.")
def svg2png(input_svg: str | Path) -> Optional[bytes]:
	"""Render SVG into PNG

	Args:
		input_svg (str | Path): input SVG's path or SVG code

	Returns:
		Optional[bytes]: PNG data
	"""

	if (input_path := Path(input_svg)).exists() and input_path.is_file():
		svg_path2png_path(input_path)
	else:
		return svg_code2png_bin(input_svg)

def svg_path2png_path(input_path: Path, output_path: Optional[Path] = None) -> None:
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
	
	svg_code2png_path(input_code, output_path, input_path=input_path)

def svg_path2png_bin(input_path: Path) -> bytes:
	"""Render SVG file and return PNG as bytes

	Args:
		input_path (Path): input SVG's path

	Returns:
		bytes: PNG data
	"""
	
	with open(input_path, 'r') as input_file:
		input_code = input_file.read()
	
	return svg_code2png_bin(input_code, input_path=input_path)


def svg_code2png_path(input_code: str, output_path: Path, input_path: Optional[Path] = None) -> None:
	"""Render provided SVG code into a PNG file

	Args:
		input_code (str): SVG code
		output_path (Path): output PNG's path
		input_path (Optional[Path]): input SVG's path (for error messages)
	"""
	
	with open(output_path, 'wb') as output_file:
		output_file.write(svg_code2png_bin(input_code, input_path=input_path))

def svg_code2png_bin(input_code: str, input_path: Optional[Path] = None) -> bytes:
	"""Render provided SVG code and return PNG as bytes

	Args:
		input_code (str): SVG code
		input_path (Optional[Path]): input SVG's path (for error messages)

	Returns:
		bytes: PNG data
	"""

	return render(input_code)