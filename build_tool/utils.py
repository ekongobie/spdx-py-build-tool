import os, sys
from distutils.sysconfig import get_python_lib

def read(filename):
    """Return the contents of a file.

    :param filename: file path
    :type filename: :class:`str`
    :return: the file's content
    :rtype: :class:`str`
    """
    with open(filename) as f:
        return f.read()


def get_virtual_env_dir():
    if "VIRTUAL_ENV" in os.environ:
        return os.environ['VIRTUAL_ENV']
    return None

def get_python_version():
    return sys.version[:3]

def get_venv_dep_dir():
    return get_python_lib()

def get_dependencies():
    """
    Get python dependencies from virtualenv.
    If they are not available(user uses another virtualenv), download them to temp folder.
    """
    dep_list = os.listdir(get_venv_dep_dir())
    print("dep_list")
    print(dep_list)
