from distutils.core import setup
import py2exe
import sys
import os 

setup(console=["gui.py"],
	options={
       "py2exe":{
            "skip_archive": True
                }
        }


	)