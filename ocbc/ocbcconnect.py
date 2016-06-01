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
"""This module contains object that represents base class for ccbc connections."""

from ocbc.utils import request
from ocbc.utils import headers

class OcbcConnect(object):
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get(self, args=None):
        url = self.url
        if args is not None:
            url = "{0}/{1}".format(url, args)

        return request.get(url, headers=headers.get(self.token))