from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="global_tools_func",
    version="0.1.0",
    author="Original Author",
    author_email="author@example.com",
    description="A collection of global tools and functions for financial data processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quantdata03/global_tools_func",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "global_tools_func": [
            "config_path/*.xlsx",
            "static_data/*.xlsx",
            "static_data/*.csv",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "numpy",
        "scipy",
        "openpyxl",
    ],
) 