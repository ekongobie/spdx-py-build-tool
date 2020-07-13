import os
import pytest
from build_tool.utils import get_dependencies
from build_tool.tool import build_parser
from build_tool.helpers import get_dependencies_file_paths, get_identifiers_for_paths

PROJECT_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "sample_project",
)

SPDX_FILE_NAME = "filenameexample"
FILE_NAME1_IN_PROJECT = "bitbake-worker"
FILE_NAME2_IN_PROJECT = "bitbake-diffsigs"

IDENTIFIER_EX1 = {
    "FileName": os.path.join(PROJECT_DIR, FILE_NAME1_IN_PROJECT),
    "SPDXID": "GPL-2.0-only",
    "scanned": True,
    "FileType": None,
    "FileChecksum": None,
}

IDENTIFIER_EX2 = {
    "FileName": os.path.join(PROJECT_DIR, FILE_NAME2_IN_PROJECT),
    "SPDXID": "GPL-2.0-only",
    "scanned": True,
    "FileType": None,
    "FileChecksum": None,
}


class TestUtils:
    def test_get_dependencies(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME])
        deps = get_dependencies(args)
        assert PROJECT_DIR in deps

    def test_deps_file_paths(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME])
        deps = get_dependencies(args)
        deps_l = get_dependencies_file_paths(deps)
        assert os.path.join(PROJECT_DIR, FILE_NAME1_IN_PROJECT) in deps_l
        assert os.path.join(PROJECT_DIR, FILE_NAME2_IN_PROJECT) in deps_l

    def test_get_identifiers_for_paths(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME])
        deps = get_dependencies(args)
        deps_l = get_dependencies_file_paths(deps)
        glob_to_skip = []
        all_identifiers = get_identifiers_for_paths(deps_l, glob_to_skip)
        assert IDENTIFIER_EX1 in all_identifiers
        assert IDENTIFIER_EX2 in all_identifiers
