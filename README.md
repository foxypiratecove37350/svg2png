svg2png is a Python package that provides a simple function to convert SVG (Scalable Vector Graphics) files into PNG (Portable Network Graphics) format. The conversion is performed using Inkscape, a powerful vector graphics editor.

### Features:
- **SVG to PNG Conversion**: Utilizes Inkscape to handle the conversion.
- **Validation**: Checks if the input file is a valid SVG and if Inkscape is installed and accessible.
- **Error Handling**: Provides meaningful error messages if the SVG file is invalid or if Inkscape is not found.

### Usage:
To convert an SVG file to PNG, simply call the `svg2png` function with the path to your SVG file:

```python
from svg2png import svg2png

svg2png('path/to/your/icon.svg')
```

### Requirements:
- **Inkscape**: Ensure that Inkscape is installed and added to your system PATH.