import py2exe
from setuptools import setup, find_packages

"""
This is a setup.py script generated by py2applet
Usage: python setup.py py2app
"""
with open("README.md", "r") as fh:
    long_description = fh.read()

with open("app/requirements.txt") as f:
    app_requirements = f.read().splitlines()

APP = ["./app/app.py"]
DATA_FILES = []
OPTIONS = {
    "packages": [
        "flask",
        "werkzeug",
        "config",
        "jinja2",
        "sqlalchemy",
        "flask",
        "sqlalchemy.dialects.sqlite",
        "wtforms",
        "flask_bootstrap",
        "selenium",
        "requests",
    ],
    "resources": ["./app/templates", "./app/static", "./app/config.json"],
    "plist": {},
}

setup_requirements = ["py2app", "setuptools>=40.5.0"]

setup(
    name="cloudsnap-analytics",
    long_description=long_description,
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=setup_requirements + app_requirements,
    packages=find_packages(include=["app"]),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License",
        "Operating System :: OS Independent",
    ),
    install_requires=app_requirements,
)
