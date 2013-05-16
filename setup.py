from distutils.core import setup
import sys
import py2exe
from glob import glob

sys.path.append("C:\\Program Files/(x86)\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT")

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup(console=['Experimental_Game.py'], data_files = data_files)
