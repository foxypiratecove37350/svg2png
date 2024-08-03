""""
Convert a SVG file into a PNG file using Inkscape
"""

import subprocess
import xml.etree.ElementTree as ET

def svg2png(inputfile):
    """
    Convert a SVG file into a PNG file using Inkscape

    Args:  
        inputfile (str): Path to the SVG file.

    Returns:
        None

    Raises:  
        ValueError: If the SVG file isn't valid or if Inkscape isn't installed/in the ``PATH``.

    Example:
        >>> svg2png('icon.svg')
        None
    """

    try:
        ET.parse(inputfile)
    except ET.ParseError:
        raise ValueError("The file isn't a valid SVG")

    try:
        subprocess.check_call(
            [
                'inkscape',
                '--export-type=png',
                inputfile
            ]
        )
    except:
        raise ValueError("Inkscape is not installed or not in the PATH")
