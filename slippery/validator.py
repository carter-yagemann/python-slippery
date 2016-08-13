#    Copyright 2016 Carter Yagemann
#
#    This file is part of python-slippery.
#
#    python-slippery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    python-slippery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with python-slippery.  If not, see <http://www.gnu.org/licenses/>.

"""Methods to validate parameters"""

def validate_id(new_id):
    """Validate an inbox id.

    Args:
      new_id:
        The id to validate.

    Return:
      True if it is a valid id, otherwise False.
    """
    if len(new_id) == 5:
        return True
    return False

def validate_key(key):
    """Validate an inbox key.

    Args:
      key:
        The key to validate.

    Return:
      True if it is a valid key, otherwise False.
    """
    if len(key) == 16:
        return True
    return False
