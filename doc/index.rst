.. python-slippery documentation master file, created by
   sphinx-quickstart on Fri Aug 12 16:39:24 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-slippery's documentation!
===========================================

Contents:

.. toctree::
   :maxdepth: 1

   installing
   getting_started
   license
   

Introduction
------------

This library provides a pure Python abstraction for the burner email website
`Slippery <http://slippery.email>`_. It works with Python 2.x.

Slippery is a website that allows users to create temporary burner email addresses
to receive emails. This is useful for testing email services or for filling out forms
that force you to provide an email address.

Since the site has no API, I decided to create this library. The library supports
creating new burner email addresses, checking for emails, and fetching their
contents. In the spirit of burners, the library also supports SOCKS5 proxies should
you want to interact with Slippery via a SSH tunnel, tor, or other proxy.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

