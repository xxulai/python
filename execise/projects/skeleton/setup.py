#-*- utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Project test",
    "author": "Lai",
    "version":"0.1",
    "install_requires":["nose"],
    "packages":["NAME"],
    "name":"TestProject",
    "scripts":[]
}

setup(**config)