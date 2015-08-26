from distutils.core import setup
import py2exe
import sys 
import py2exe 
from distutils.core import setup

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")
setup(
    windows = [
    {
        "script": "main.py"
    }
    ],
    console=['main.py'], options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}}

)