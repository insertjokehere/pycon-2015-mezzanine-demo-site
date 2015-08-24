#!/usr/bin/env python3
from setuptools import setup, find_packages

# Get the dependancies out of our requirements file
# This will fail if the requirements file contains external references
with open("./requirements/common.txt") as f:
    reqs = [r for r in f.read().splitlines() if not r.startswith("#")]

setup(
    name="pycon_demo",
    version='0.0.0',
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pycon_demo = pycon_demo:management_command',
        ],
    }
)
