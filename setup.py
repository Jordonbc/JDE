#!python3.4
import sys
from cx_Freeze import setup, Executable

# None for commandline or "Win32GUI" or GUI

base = "Win32GUI"


dataFiles = ["JDE/", "Programs/", "Users/"]
modules = ["logging", "tkinter", "PIL"]

setup(name="JDE",
      version="1.5.0a",
      author="Jordon Brooks",
      url="https://jordonbc.github.io",
      options = {'build_exe': {'include_files':dataFiles, 'packages': modules}}, 
      description="Editor",
      executables = [Executable("run.py", base=base, icon="icon.ico")])
