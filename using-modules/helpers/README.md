
# Hiding module entities.
# How do you hide things/prevent things in a module from being exposed?
# __all__
# Look at helpers.


# the module search path.
# Where do import statments import from? How can we modify that?
# import statements pull from
# 1) Current working directory
# 2) If you set the PYTHONPATH environment variable before running python, you can add directories to include in the import search
# 3) There are directories that your python installation knows about that you can import standard library entties from or any
# 3rd party entities you install can be imported from
# you can find out what these directories are by:
"""
>>> import sys
>>> sys.path
['', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
 '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
 '/Users/huntaj/dev/pythoncertification/venv/lib/python3.7/site-packages']
"""
# '' is current directory.
# site-packages contains 3rd party installations

"""
(venv) Austins-iMac:using-modules huntaj$ cd ..
(venv) Austins-iMac:pythoncertification huntaj$ touch example_mod.py
(venv) Austins-iMac:pythoncertification huntaj$ PYTHONPATH='/Users/huntaj/dev/pythoncertification/' python3.7
Python 3.7.7 (default, Mar 26 2020, 18:08:50)
[Clang 11.0.3 (clang-1103.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import example_mod
>>> import sys
>>> sys.path
['', '/Users/huntaj/dev/pythoncertification', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
'/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7',
'/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload',
'/Users/huntaj/dev/pythoncertification/venv/lib/python3.7/site-packages']
"""

"""
Custom vs. Standard Lib imports (same name. Which takes priority? Stdlib.)

(venv) Austins-iMac:pythoncertification huntaj$ touch sys.py
(venv) Austins-iMac:pythoncertification huntaj$ PYTHONPATH='/Users/huntaj/dev/pythoncertification/' python3.7
Python 3.7.7 (default, Mar 26 2020, 18:08:50)
[Clang 11.0.3 (clang-1103.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/Users/huntaj/dev/pythoncertification', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/usr/local/Cellar/python/3.7.7/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/huntaj/dev/pythoncertification/venv/lib/python3.7/site-packages']
>>> print("Even though interpreter searches sys.path in order, it FIRST searches standard library, so sys module used here is still from standard lib even though its in pythoncertification folder. This prevents stdlib entities from being overwritten")
Even though interpreter searches sys.path in order, it FIRST searches standard library, so sys module used here is still from standard lib even though its in pythoncertification folder. This prevents stdlib entities from being overwritten
>>>
"""


# Distributing and Installing Packages

### pip = command line utility for installing packages from pypi.org (python package index)
``` pip --help
Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.

```
# Creating an installable package.
# Let helpers (inside using-modules) be the package we want to set up and distribute.
```
cd using-modules
mkdir -p helpers/src/helpers
# Outer helpers will be where all the packaging code is stored for bundling up code.
# src/helpers will be the source code of the package.
mv helpers/*.py helpers/src/helpers/
(venv) Austins-iMac:using-modules huntaj$ tree helpers/
helpers/
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── strings.cpython-37.pyc
│   └── variables.cpython-37.pyc
└── src
    └── helpers
        ├── __init__.py
        ├── strings.py
        └── variables.py

3 directories, 6 files

# PyPA -> Python Packaging Authority
github.com/pypa/sampleproject

cd helpers
# Create a setup.py file. Can just pull it from sample project.
curl -O https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py

```
What is a distributioN?
Single file that can be pip installed.
2 formats: wheel, egg
egg is historic, wheel is modern
pip reads wheel, unpacks source code into the site-packages directory (3rd party packages)
How to build the wheel?
First install it.
```
(venv) Austins-iMac:helpers huntaj$ pip install --upgrade wheel
(venv) Austins-iMac:helpers huntaj$ python setup.py --help-commands
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  check             perform some checks on the package
  upload            upload binary package to PyPI

Extra commands:
  THIS bdist_wheel       create a wheel distribution; build a distribution that is a wheel!
  alias             define a shortcut to invoke one or more commands
  bdist_egg         create an "egg" distribution
  develop           install package in 'development mode'
  dist_info         create a .dist-info directory
  easy_install      Find/get/install Python packages
  egg_info          create a distribution's .egg-info directory
  install_egg_info  Install an .egg-info directory for the package
  rotate            delete older distributions, keeping N newest files
  saveopts          save supplied options to setup.cfg or other config file
  setopt            set an option in setup.cfg or another config file
  test              run unit tests after in-place build
  upload_docs       Upload documentation to PyPI

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help

```
we want python setup.py bdist_wheel # build a distribution that is in wheel format
```
(venv) Austins-iMac:helpers huntaj$ python setup.py bdist_wheel
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/helpers
copying src/helpers/variables.py -> build/lib/helpers
copying src/helpers/__init__.py -> build/lib/helpers
copying src/helpers/strings.py -> build/lib/helpers
installing to build/bdist.macosx-10.15-x86_64/wheel
running install
running install_lib
creating build/bdist.macosx-10.15-x86_64
creating build/bdist.macosx-10.15-x86_64/wheel
creating build/bdist.macosx-10.15-x86_64/wheel/helpers
copying build/lib/helpers/variables.py -> build/bdist.macosx-10.15-x86_64/wheel/helpers
copying build/lib/helpers/__init__.py -> build/bdist.macosx-10.15-x86_64/wheel/helpers
copying build/lib/helpers/strings.py -> build/bdist.macosx-10.15-x86_64/wheel/helpers
running install_egg_info
running egg_info
creating src/helpers.egg-info
writing src/helpers.egg-info/PKG-INFO
writing dependency_links to src/helpers.egg-info/dependency_links.txt
writing top-level names to src/helpers.egg-info/top_level.txt
writing manifest file 'src/helpers.egg-info/SOURCES.txt'
reading manifest file 'src/helpers.egg-info/SOURCES.txt'
writing manifest file 'src/helpers.egg-info/SOURCES.txt'
Copying src/helpers.egg-info to build/bdist.macosx-10.15-x86_64/wheel/helpers-1.0.0-py3.7.egg-info
running install_scripts
creating build/bdist.macosx-10.15-x86_64/wheel/helpers-1.0.0.dist-info/WHEEL
creating 'dist/helpers-1.0.0-py3-none-any.whl' and adding 'build/bdist.macosx-10.15-x86_64/wheel' to it
adding 'helpers/__init__.py'
adding 'helpers/strings.py'
adding 'helpers/variables.py'
adding 'helpers-1.0.0.dist-info/METADATA'
adding 'helpers-1.0.0.dist-info/WHEEL'
adding 'helpers-1.0.0.dist-info/top_level.txt'
adding 'helpers-1.0.0.dist-info/RECORD'
removing build/bdist.macosx-10.15-x86_64/wheel
(venv) Austins-iMac:helpers huntaj$ ls dist/
helpers-1.0.0-py3-none-any.whl
```

# Doctests! Automated testing within Documentation (Method docstring) formatted as REPL input followed by expected output.
```
(venv) Austins-iMac:helpers huntaj$ python -m doctest src/helpers/strings.py --verbose
__name__ in helpers.py: strings
Trying:
    extract_upper("HELLo theRe BOB")
Expecting:
    ['H', 'E', 'L', 'L', 'R', 'B', 'O', 'B']
ok
2 items had no tests:
    strings
    strings.extract_lower
1 items passed all tests:
   1 tests in strings.extract_upper
1 tests in 3 items.
1 passed and 0 failed.
Test passed.
```