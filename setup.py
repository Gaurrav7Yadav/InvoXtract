import os
from pathlib import Path

from setuptools import setup

PKG_NAME = "python-doctr"
VERSION = os.getenv("BUILD_VERSION", "0.11.1a0")


if __name__ == "__main__":
    print(f"Building wheel {PKG_NAME}-{VERSION}")

    # Dynamically set the __version__ attribute
    cwd = Path(__file__).parent.absolute()
    with open(cwd.joinpath("doctr", "version.py"), "w", encoding="utf-8") as f:
        f.write(f"__version__ = '{VERSION}'\n")

    setup(name=PKG_NAME, version=VERSION)
