from setuptools import setup
import sys

setup(
    name="TETyper",
    version="1.2.dev",
    url="https://github.com/aesheppard/TETyper",
    author="Anna Sheppard",
    author_email="anna.sheppard@ndm.ox.ac.uk",
    description="transposable element typing pipeline",
    license="GPL",
    keywords="TE typing NGS",
    classifiers=[
        'Development Status :: 5 - Production/Stable'
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python'
    ],
    install_requires=[
        'biopython',
        'pysam',
        'PyVCF'
    ],
    scripts=[
        'tetyper/TETyper.py'
    ],
    include_package_data=True,
)
