# -*- coding: utf-8 -*-
"""
Created on Tue Oct  10 18:43 2023
 Set up file for the tensor calculator
@author: Vera Hui López
"""

from setuptools import setup, find_packages
from module_structure import __author__,__version__,__name__


VERSION = __version__
AUTHOR = __author__
NAME = __name__

setup(
    name                    = 'tensor-calculator',
    version                 = '1.0.0',
    description             = ' Package for Operations apply to tensors of your desire dimensions',
    author                  = "Vera Hui López García",
    author_email            = '9000429@alumnos.ufv.es',
    license                 = 'MIT',
    python_requires         = '>=3.9.5',
    packages                = find_packages(),
    include_package_data    = True,
    package_data            = {'': ['resources/*.csv','resources/clusters/*.csv']},
    install_requires        = [
                                'pandas',
                                'numpy',
                                'torch'
                                ]
     )