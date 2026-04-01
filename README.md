# `svg2png`

`svg2png` is a Python package that provides a simple function to convert SVG graphics
into PNG format.

## Installation

```shell
pip install `svg2png`
```

## Features

- Both files and direct content
- To files or return binary stream
- **SVG 1.1 2nd Edition**

## Usage

To convert an SVG file to PNG, simply call the `svg2png` functions with the path
to your SVG file:

```python
import svg2png

svg2png.svg2png('file.svg') # auto redirect to the appropriate function, deprecated
png_bin: bytes = svg2png.svg_path2png_bin('file.svg')
svg2png.svg_path2png_path('file.svg', 'new.png') # output optional, defaults to [filename].png
svg2png.svg_code2png_path('<svg xmlns="...">...</svg>', 'file.png')
png_bin: bytes = svg2png.svg_code2png_bin('<svg xmlns="...">...</svg>')
```
