import os
import pytest
from build_tool.tool import build_parser

PROJECT_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "sample_project",
)

SPDX_FILE_NAME = "filenameexample"


class TestTool:
    def test_parser_project_path(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME])
        assert PROJECT_DIR == args.project_path
        assert False == args.tv == False
        assert False == args.rdf == False
        assert False == args.res == False

    def test_parser_file_name(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME])
        assert args.spdx_file_name == SPDX_FILE_NAME
        assert False == args.tv == False
        assert False == args.rdf == False
        assert False == args.res == False

    def test_parser_tagvalue_arg(self):
        args = build_parser([PROJECT_DIR, "mg", "--tv"])
        assert args.tv == True
        assert False == args.rdf == False
        assert False == args.res == False

    def test_parser_rdf_arg(self):
        args = build_parser([PROJECT_DIR, "mg", "--tv", "--rdf"])
        assert args.rdf == True
        assert args.res == False

    def test_parser_res_arg(self):
        args = build_parser([PROJECT_DIR, "mg", "--tv", "--rdf", "--res"])
        assert args.res == True
