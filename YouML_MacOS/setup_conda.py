
from setuptools import setup, find_packages
import platform


if platform.python_version() != '3.7.11':
    print("To install YouML, your python version has to be 3.7.11\nIt's recommended to create a virtual environment with a python of 3.7.11")
    exit(0)
    

setup(

    author = 'Chongya Song',
    author_email = 'schongy523@gmail.com',
    url = 'https://www.linkedin.com/in/chongya-song/',

    name = 'YouML',
    version = '0.6',
    description = 'A Machine Learning Toolkit',
    long_description = 'YouML stands for “Your (free) Machine Learning (toolkit).” It intends to provide the machine learning community a free and no-code toolkit for preprocessing data and building machine learning models. Several key features will be released after no major bug can be found in the current version. The ultimate goal is to deliver a platform where users can obtain solutions to address tough problems in their machine learning tasks.',
    platforms = 'MacOS, Linux, Windows Subsystem for Linux (WSL)',

    packages = find_packages(),
    include_package_data=True,
    entry_points = {'gui_scripts': ['YouML = YouML.Main:start']},
    
    python_requires = '==3.7.11',

    zip_safe = False,

    )
