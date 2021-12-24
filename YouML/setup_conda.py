
from setuptools import setup, find_packages


setup(

    author = 'Chongya Song',
    author_email = 'schongy523@gmail.com',
    url = 'https://www.linkedin.com/in/chongya-song/',

    name = 'YouML',
    version = '0.6',
    description = 'A Machine Learning Toolkit',
    long_description = 'YouML stands for “Your (free) Machine Learning (toolkit).” It intends to provide the machine learning community a free and no-code toolkit for preprocessing data and building machine learning models. Several key features will be released after no major bug can be found in the current version. The ultimate goal is to deliver a platform where users can obtain solutions to address tough problems in their machine learning tasks.',
    platforms = 'MacOS',

    packages = find_packages(),
    include_package_data=True,
    entry_points = {'gui_scripts': ['YouML = YouML.Main:start']},

    zip_safe = False,

    )
