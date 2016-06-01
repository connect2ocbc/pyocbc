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
"""This module contains object that represents ocbc.Branch."""

from ocbc.base import OcbcObject


class Branch(OcbcObject):
    def __init__(self, address, landmark, latitude, longitude, postalCode, **kwargs):
        self.address = address
        self.landmark = landmark
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.postalCode = postalCode

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):

        Returns:
            ocbc.Branch:
        """
        if not data:
            return None

        return Branch(**data)