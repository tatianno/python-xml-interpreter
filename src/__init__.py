import os
import sys


DIR = os.path.join(os.path.dirname(__file__))
sys.path.append(DIR)


from parsers import XmlParser

__all__ = [
    'XmlParser'
]