
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="bitnob",
    version="1.0.9",
    description="Python SDK for the Bitnob\"s API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bitnob/bitnob_python_sdk",
    author="Bitnob",
    author_email="info@bitnob.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["requests"],
    packages=find_packages(),
    python_requires=">=3.6"
)