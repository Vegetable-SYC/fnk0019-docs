# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
from datetime import datetime
import os
import pathlib
import sys
from freenove import freenove

syc = freenove

syc.docs_init(Freenove_Super_Starter_Kit_for_ESP8266, 66)

def setup(app):
    pass
   
# >>> BEGIN BASE CONFIG (AUTO-GENERATED)
# !!! DO NOT EDIT THIS SECTION MANUALLY !!!
# <<< END BASE CONFIG

# === BEGIN PROJECT-SPECIFIC CONFIG ===
# （原来的所有配置内容保持在这里不变）