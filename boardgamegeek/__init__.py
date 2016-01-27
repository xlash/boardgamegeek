# coding: utf-8
"""
.. module:: boardgamegeek
   :platform: Unix, Windows
   :synopsis: interface to boardgamegeek.com

.. moduleauthor:: Cosmin Luță <q4break@gmail.com>
"""
__import__('pkg_resources').declare_namespace(__name__)

from .api import BoardGameGeek
from .exceptions import BoardGameGeekError, BoardGameGeekAPIRetryError, BoardGameGeekAPIError, BoardGameGeekTimeoutError
from .version import __version__

__all__ = [BoardGameGeek, BoardGameGeekAPIRetryError, BoardGameGeekError, BoardGameGeekAPIError, BoardGameGeekTimeoutError]
