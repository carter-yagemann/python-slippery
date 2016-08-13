Python Slippery

A python library for interacting with the burner email website slippery.email.

By `Carter Yagemann <carter.yagemann@gmail.com>`_

============
Introduction
============

This library provides a pure Python abstraction for the burner email website
`Slippery <http://slippery.email>`_. It works with Python 2.x.

Slippery is a website that allows users to create temporary burner email addresses
to receive emails. This is useful for testing email services or for filling out forms
that force you to provide an email address.

Since the site has no API, I decided to create this library. The library supports
creating new burner email addresses, checking for emails, and fetching their
contents. In the spirit of burners, the library also supports SOCKS5 proxies should
you want to interact with Slippery via a SSH tunnel, tor, or other proxy.

==========
Installing
==========

You will need to install python-slippery's dependencies::

    $ pip install -Ur requirements.txt

and then you can import the module.

=====
Usage
=====

---------------
Getting Started
---------------

The core of the library is the `BurnerEmail` object. Here are some
examples on how to use it::

    from slippery.burner_email import BurnerEmail
    
    email = BurnerEmail.generate()              # create a new email address
    print email.getmailto()                     # send emails here!
    email.setinbox('aaaaa', 'aaaaaaaaaaaaaaaa') # use this instead of generate if you
                                                # already have an email
    msgs = email.fetch_emails()                 # see what's in the inbox
    print email.fetch_email('12345')            # get the contents of an email
    email.delete_email('12345')                 # delete an email

When you use the method `fetch_emails()` it returns an array of dictionaries with
the following form::

    {'id':int, 'sender':str, 'subject':str, 'date':str}

`id` is what should be passed to `fetch_email()` and `delete_email()`.

The library also includes a useful method for setting a SOCKS5 proxy::

    from slippery import proxy
    proxy.set_proxy('localhost', '9050')

And that's it! Super simple. There's also an example of a very simple console
program in the examples directory of the repo.

-------------
Documentation
-------------

Documentation is available via pydoc::

    $ pydoc slippery.[model]

-------
License
-------

Copyright 2016 Carter Yagemann

This file is part of python-slippery.

python-slippery is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python-slippery is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with python-slippery.  If not, see <http://www.gnu.org/licenses/>.
