"""
This module contains the Scope phenomenological taxonomy.
"""

__version__ = '0.2.0'
__all__ = ["__version__", "taxonomy"]

import os
from os.path import join
import yaml
from yaml import FullLoader

tax_path = join(os.path.dirname(__file__), 'phenomenological.yaml')

with open(tax_path) as taxonomy_yaml:
    taxonomy = yaml.load(taxonomy_yaml, Loader=yaml.FullLoader)
