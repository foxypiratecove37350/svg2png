""""
Render an SVG file into a PNG file
"""

from typing import Optional
from lxml import etree
from pathlib import Path

from .errors import InvalidSVGError

def svg2png(input: str | Path) -> Optional[bytes]:
    """
    Render an SVG file into a PNG file

    Args:  
        input (str): Path to the SVG file or SVG content.

    Returns:
        None

    Raises:  
        InvalidSVGError: If the SVG content isn't valid.

    Example:
        >>> svg2png('icon.svg')
        None
    """

    raise NotImplementedError

def svg_path2png_path(input_path: Path, output_path: Optional[Path]) -> None:
    raise NotImplementedError

def svg_path2png_bin(input_path: Path) -> bytes:
    raise NotImplementedError

def svg_code2png_path(input_code: str, output_path: Path) -> None:
    raise NotImplementedError

def svg_code2png_bin(input_code: str) -> bytes:
    raise NotImplementedError