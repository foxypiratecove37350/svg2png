from setuptools import setup, find_packages # type: ignore
from svg2png import version

setup(
    name='svg2png',
    version=version,
    packages=find_packages(),
    install_requires=[],
    author='foxypiratecove37350',
    author_email='foxypiratecovefnaf12@gmail.com',
    description='Convert a SVG file into a PNG file using Inkscape',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/foxypiratecove37350/svg2png',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
    ],
    license='GPL-2.0',
)
