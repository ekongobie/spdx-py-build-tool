import os
import pytest
from build_tool.tool import build_parser, create_spdx_document
from build_tool.utils import FILE_SUFFIX

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
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME, "--tv"])
        assert args.tv == True
        assert False == args.rdf == False
        assert False == args.res == False

    def test_parser_rdf_arg(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME, "--tv", "--rdf"])
        assert args.rdf == True
        assert args.res == False

    def test_parser_res_arg(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME, "--tv", "--rdf", "--res"])
        assert args.res == True

    def test_create_spdx_document(self):
        args = build_parser([PROJECT_DIR, SPDX_FILE_NAME, "--tv"])
        create_spdx_document(args)
        file_path = os.path.join(PROJECT_DIR, SPDX_FILE_NAME + FILE_SUFFIX + ".spdx")
        assert os.path.exists(file_path) == True
        os.remove(file_path)
        assert os.path.exists(file_path) == False
