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

from slippery.burner_email import BurnerEmail

def test_burner_init():
    email = BurnerEmail()
    assert email != None
    assert email._id == None
    assert email._key == None
    assert email._url == None
    assert email._mailto == None

def test_burner_generate():
    email = BurnerEmail().generate()
    assert email != None
    assert email._id != None
    assert email._key != None
    assert email._url != None
    assert email._mailto != None
    assert len(email._id) == 5
    assert len(email._key) == 16
    assert len(email._url) == 50
    assert len(email._mailto) == 16

def test_burner_setinbox():
    email = BurnerEmail().setinbox('aaaaa', 'abcdefghijklmnop')
    assert email != None
    assert email._id != None
    assert email._key != None
    assert email._url != None
    assert email._mailto != None
    assert len(email._id) == 5
    assert len(email._key) == 16
    assert len(email._url) == 50
    assert len(email._mailto) == 16

def test_burner_setinbox_id_validation():
    try:
        email = BurnerEmail().setinbox('aaaa', 'abcdefghijklmnop')
    except ValueError:
        return
    assert False

def test_burner_setinbox_key_validation():
    try:
        email = BurnerEmail().setinbox('aaaaa', 'abcdefghijklmno')
    except ValueError:
        return
    assert False

def test_getid():
    email = BurnerEmail().setinbox('aaaaa', 'abcdefghijklmnop')
    assert len(email.getid()) == 5

def test_getkey():
    email = BurnerEmail().setinbox('aaaaa', 'abcdefghijklmnop')
    assert len(email.getkey()) == 16

def test_getmailto():
    email = BurnerEmail().setinbox('aaaaa', 'abcdefghijklmnop')
    assert len(email.getmailto()) == 16

def test_getinbox():
    email = BurnerEmail().setinbox('aaaaa', 'abcdefghijklmnop')
    assert len(email.getinbox()) == 50
