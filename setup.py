
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import imp, os
from build_tool.utils import read

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

metadata = imp.load_source(
    'metadata', os.path.join(ROOT_DIR, 'build_tool/metadata.py'))

setup_dict = dict(
    name=metadata.package,
    version=metadata.version,
    author=metadata.authors[0],
    author_email=metadata.emails[0],
    maintainer=metadata.authors[0],
    maintainer_email=metadata.emails[0],
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.md'),
    license=read('LICENSE'),
    entry_points={
        'console_scripts': [
            'spdx-build = build_tool.tool:entry_point',
        ],
    }
)


def main():
    setup(**setup_dict)


if __name__ == '__main__':
    main()
