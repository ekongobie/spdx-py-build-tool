# Python SPDX plugin
How can we seamlessly generate spdx documents in packages via their package managers?


## Introduction:
This project aims to ease the process of creation of spdx documents for packages with the use of the python build tool, that is, PIP.
Given that pip is constantly being updated, we opted for a more direct approach, not using SBOMs which could change in the future. This approach consists of programmatically getting the list of all files in the given project/package, their dependencies, extracting the license information from each file and then using that information to generate the spdx document with the use of the spdx project tools-python.

## Environment:
Inorder to guarantee that the tool functions properly nor matter the environment, this tool is hosted on pypi and therefore installable on most operating systems, for use with python projects.
So, wherever you are developing python a python project and are using pip to install dependencies, you can use this tool without any quacks.

## Usage:
It is best practice to develop python project in a virtualenv. This was taken into account during the development of this tool; however, it is not a prerequisite. If you are not in a virtualenv, the generated spdx document might be messy.
So, please use a virtualenv.
Activate the virtualenv.
Install the tool, using pip: `pip install --`
Inorder to generate the spdx document for a given project, run `spdx-build project_path  spdx_file_name --tv`
The spdx document will be generated and included in the project_path
Given the simplicity of the above, doing the same in any continuous integration tool is easy.

## Further work/improvements:
The tools repository returns an error when the spdx rdf file generation is attempted; so it fails. Once this is corrected in the tools-python repository, updates might be requires in our tool for it to function appropriately.
