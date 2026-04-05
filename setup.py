from setuptools import setup, find_packages # type: ignore
from svg2png import (
    __project_name__,
    __version__,
    __author__,
    __description__,
    __url__,
    __license__
)

setup(
    name=__project_name__,
    version=__version__,
    packages=find_packages(),
    author=__author__,
    description=__description__,
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url=__url__,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
    ],
    license=__license__,
    install_requires=open('requirements.txt', 'r', encoding='utf-8').read().splitlines()
)
