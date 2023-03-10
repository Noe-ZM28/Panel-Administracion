#!/usr/bin/env python

import os
import sys
from setuptools import find_packages, setup


base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)


def read(fname):
    """read file from same path as setup.py"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools_scm_template = """\
# coding: utf-8
# file generated by setuptools_scm
# don't change, don't track in version control

version = '{version}'
"""


setup(
    use_scm_version={
        "write_to": "src/escpos/version.py",
        "write_to_template": setuptools_scm_template,
    },
    platforms="any",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests", "tests.*"]),
    package_data={"escpos": ["capabilities.json"]},
    entry_points={"console_scripts": ["python-escpos = escpos.cli:main"]},
)