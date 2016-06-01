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
"""This module contains object that represents ocbc.Forex."""

from ocbc.ocbcconnect import OcbcConnect
from ocbc.rate import Rate


class Forex(OcbcConnect):
    def __init__(self, url, token):
        super(Forex, self).__init__(url, token)

    def all(self):
        return Forex.de_json(self.get())

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):

        Returns:
            list of ocbc.Rate:
        """
        if not data:
            return None

        rates = []
        for strjson in data['ForexRates']:
            rates.append(Rate.de_json(strjson))
        return rates
