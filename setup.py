#!/usr/bin/env python
from setuptools import find_packages, setup

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="flower_classification_model",
    version="0.0.2",
    description="scivision plugin, using EfficientNetB3 model",
    url="https://github.com/alan-turing-institute/flower_classification_model",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
)