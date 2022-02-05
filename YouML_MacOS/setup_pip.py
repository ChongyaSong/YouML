
from setuptools import setup, find_packages


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

    install_requires =
                        [
                            'xlrd',
                            'tqdm',
                            'apsw',
                            'blist',
                            'cycler',
                            'psutil',
                            'slugify',
                            'urllib3',
                            'requests',
                            'openpyxl',
                            'pycryptodome',

                            'scikit-learn-intelex==2021.4.0',
                            'scikit-learn==0.24.2',
                            'matplotlib==3.4.2',
                            'pandas==1.3.2',
                            'numpy==1.20.3',
                            'scipy==1.7.1',
                            'pyqt5==5.9.2',
                        ],

    zip_safe = False,

    )
