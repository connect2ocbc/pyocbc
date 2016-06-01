#!/usr/bin/env python
#
# A library that provides a Python interface to the OCBC API
# Copyright (C) 2016
# Naveen Sanmane <naveen.sanmane@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""A library that provides a Python interface to the OCBC API"""

from sys import version_info

from .base import OcbcObject
from .ocbcconnect import OcbcConnect
from .nullhandler import NullHandler
from .error import OcbcError
from .error import Unauthorized
from .forex import Forex
from .rate import Rate
from .branches import Branches
from .branch import Branch
from .atms import Atms
from .atm import Atm
from .ccsuggest import CCSuggest
from .creditcard import CreditCard

__author__ = 'naveen.sanmane@gmail.com'
__version__ = '1.0.0'
__all__ = ['OcbcObject', 'OcbcConnect', 'Forex', 'Rate', 'Branches', 'Branch',
           'Atms', 'Atm', 'CCSuggest', 'CreditCard', 'OcbcError', 'Unauthorized',
           'NullHandler',]