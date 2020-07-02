import sys, os
import argparse
from .utils import get_dependencies
from .core import SPDXFile
from .helpers import get_identifiers_for_paths, get_dependencies_file_paths

def build_parser():
    parser = argparse.ArgumentParser(description='Python SPDX Build Tool Plugin')
    parser.add_argument('project_path', help='Path to project to build.')
    parser.add_argument('spdx_file_name', help='Name of spdx file to create. Default is project name.')
    parser.add_argument('--tv', help='output tag-value spdx file', action='store_true')
    parser.add_argument('--rdf', help='output rdf spdx file', action='store_true')
    parser.add_argument('--res', help='Scan python files with reserved names?', action='store_true')
    return parser


def print_arguments(args):
    print("Tag-value?: " + str(args.tv))
    print("RDF?: " + str(args.rdf))
    print("Scan reserved names?: " + str(args.res))


def create_spdx_document(args):
    deps = get_dependencies(args)
    glob_to_skip = []
    file_types = "tv"
    deps_l = get_dependencies_file_paths(deps)
    all_identifiers = get_identifiers_for_paths(deps_l, glob_to_skip)
    print("all_identifiers")
    print(len(all_identifiers))
    spdx_file = SPDXFile(args.project_path, args.spdx_file_name, all_identifiers, True, file_types)
    print(len(spdx_file.id_scan_results))
    spdx_file.create_spdx_document()


def main(argv):
    parser = build_parser()
    args = parser.parse_args()
    print_arguments(args)
    create_spdx_document(args)
)

def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
