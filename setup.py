import mtb
import sys

_no_data_files = "--no-data-files"
no_data_files = False
if _no_data_files in sys.argv:
    no_data_files = True
    sys.argv.remove(_no_data_files)

NAME = 'mtb'
VERSION = mtb.VERSION
DESCRIPTION = "MyToolBox - collection of tools to be shared across modules"
LONG_DESCRIPTION = """
MyToolBox is a collections of tools and libraries which are shared
between different modules which ease the life of a Python developer.
"""
AUTHOR = 'Massimo Paladin'
AUTHOR_EMAIL = 'massimo.paladin@gmail.com'
LICENSE = "ASL 2.0"
PLATFORMS = "Any"
URL = "https://github.com/mpaladin/python-mtb"
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.1",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Topic :: Software Development :: Libraries :: Python Modules"
]

from distutils.core import setup, Command


class test(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from test import run_tests
        run_tests.main()

if no_data_files:
    data_files = list()
else:
    data_files = list()
setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      platforms=PLATFORMS,
      url=URL,
      classifiers=CLASSIFIERS,
      packages=['mtb', ],
      data_files=data_files,
      cmdclass={'test': test, }, )
