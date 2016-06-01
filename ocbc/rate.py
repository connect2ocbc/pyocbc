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
"""This module contains object that represents ocbc.Rate."""

from ocbc.base import OcbcObject


class Rate(OcbcObject):
    def __init__(self, bankBuyingRateTT, bankSellingRate, fromCurrency, toCurrency, unit, **kwargs):
        self.bankBuyingRateTT = float(bankBuyingRateTT)
        self.bankSellingRate = float(bankSellingRate)
        self.fromCurrency = fromCurrency
        self.toCurrency = toCurrency
        self.unit = int(unit)

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):

        Returns:
            ocbc.Rate:
        """
        if not data:
            return None

        return Rate(**data)