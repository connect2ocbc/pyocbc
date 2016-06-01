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
"""Base class for OCBC Objects."""

from abc import ABCMeta


class OcbcObject(object):
    """Base class for most ocbc objects."""

    __metaclass__ = ABCMeta

    def __str__(self):
        return str(self.to_dict())

    def __getitem__(self, item):
        return self.__dict__[item]

    @staticmethod
    def de_json(data):
        """
        Args:
            data (str):

        Returns:
            ocbc.OcbcObject:
        """
        if not data:
            return None

        data = data.copy()

        return data

    def to_dict(self):
        """
        Returns:
            dict:
        """
        data = dict()

        for key in iter(self.__dict__):
            value = self.__dict__[key]
            if value is not None:
                if hasattr(value, 'to_dict'):
                    data[key] = value.to_dict()
                else:
                    data[key] = value

        return data



