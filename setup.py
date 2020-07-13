# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import imp, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_dict = dict(
    name="spdx_py_build_tool_ekm",
    version="0.1",
    author="Ekong Obie Philip",
    author_email="ekongobiephilip@gmail.com",
    maintainer="Ekong Obie Philip",
    maintainer_email="ekongobiephilip@gmail.com",
    url="https://github.com/spdx/",
    description="Support a continuous integration (CI) generation of SPDX files by creating a plugins or extensions to build tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["build_tool"],
    entry_points={"console_scripts": ["spdx-build = build_tool.tool:entry_point",],},
    install_requires=[
        "checksumdir==1.2.0",
        "isodate==0.6.0",
        "pip==9.0.1",
        "pkg-resources==0.0.0",
        "ply==3.11",
        "pyparsing==2.4.7",
        "rdflib==5.0.0",
        "setuptools==39.0.1",
        "six==1.15.0",
        "spdx-tools",
        "pytest",
    ],
    dependency_links=[
        "git+https://github.com/spdx/tools-python.git@276e30d5ddeae98e4cefb455b4d245506e6345b1#egg=spdx-tools"
    ],
)


def main():
    setup(**setup_dict)


if __name__ == "__main__":
    main()
