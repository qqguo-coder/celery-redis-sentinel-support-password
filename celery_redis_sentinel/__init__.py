# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals


__author__ = 'qqguuo'
__version__ = '0.0.1'

try:
    from .backend import RedisSentinelBackend  # noqa
    from .register import register  # noqa
    from .transport import SentinelTransport  # noqa
except ImportError:
    # probably importing in setup.py so make these optional imports
    pass
