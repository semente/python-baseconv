baseconv
========

.. image:: https://travis-ci.org/semente/python-baseconv.svg?branch=master
    :target: https://travis-ci.org/semente/python-baseconv

Copyright (c) 2010, 2011, 2012, 2015, 2017 Guilherme Gondim.
All rights reserved.

Copyright (c) 2009 Simon Willison.
All rights reserved.

Copyright (c) 2002 Drew Perttula.
All rights reserved.

**Description:**
    Python module to convert numbers from base 10 integers to base X strings and back again.
**Author(s):**
    Drew Perttula, Simon Willison, Guilherme Gondim
**License:**
    Python Software Foundation License version 2
**Project website:**
    https://github.com/semente/python-baseconv
**References:**
    http://www.djangosnippets.org/snippets/1431/ ;
    http://code.activestate.com/recipes/111286/

Install and Usage Instructions
------------------------------

You can use ``pip`` to install ``baseconv`` module::

    $ pip install python-baseconv

Example usage::

  >>> from baseconv import base2, base16, base36, base56, base62, base64
  >>> base2.encode(1234)
  '10011010010'
  >>> base2.decode('10011010010')
  '1234'
  >>> base64.encode(100000000000000000000000000000000000)
  '4q9XSiTDWYk7Z-W00000'
  >>> base64.decode('4q9XSiTDWYk7Z-W00000')
  '100000000000000000000000000000000000'

  >>> from baseconv import BaseConverter
  >>> base20 = BaseConverter('MyOwnAlphabet0123456')
  >>> base20.encode(1234)
  'wy1'
  >>> base20.decode('wy1')
  '1234'
  >>> base20.encode(-1234)
  '-wy1'
  >>> base20.decode('-wy1')
  '-1234'
  >>> base11 = BaseConverter('0123456789-', sign='$')
  >>> base11.encode('$1234')
  '$-22'
  >>> base11.decode('$-22')
  '$1234'

License information
-------------------

See the file "LICENSE" for terms & conditions for usage, and a
DISCLAIMER OF ALL WARRANTIES.

This baseconv distribution contains no GNU General Public Licensed (GPLed)
code, just like prior baseconv distributions.

All trademarks referenced herein are property of their respective
holders.

Django
------

The Django Project includes a copy of this module on ``django.utils.baseconv``.
