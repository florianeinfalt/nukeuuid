nukeuuid
========

.. image:: https://img.shields.io/pypi/l/nukeuuid.svg
    :target: https://pypi.python.org/pypi/nukeuuid
.. image:: https://img.shields.io/pypi/pyversions/nukeuuid.svg
    :target: https://pypi.python.org/pypi/nukeuuid
.. image:: https://img.shields.io/pypi/v/nukeuuid.svg
    :target: https://pypi.python.org/pypi/nukeuuid
.. image:: https://img.shields.io/pypi/wheel/nukeuuid.svg
    :target: https://pypi.python.org/pypi/nukeuuid
.. image:: https://readthedocs.org/projects/nukeuuid/badge/?version=latest
    :target: https://readthedocs.org/projects/nukeuuid/?badge=latest

``nukeuuid`` is a unique identifier library for Nuke. UUIDs are stored on
nodes and therefore persist Nuke sessions. UUIDs can be used to track nodes
throughout the compositing process.

`Full Documentation`_

Installation
------------

To install ``nukeuuid``, type:

.. code-block:: bash

    $ pip install nukeuuid

Open Nuke's ``init.py`` file and add:

.. code-block:: python

    nuke.pluginAddPath('/path/to/your/local/python/site-packages')

Getting Started
---------------

To get started with ``nukeuuid``, type in the Nuke Script Editor:

.. code-block:: python

    import nukeuuid

Define a dictionary of UUIDs to be set, with the keys defining the UUID name
and the values defining the UUID values.

.. note::
    The empty string as a key will evaluate to the default UUID name ``uuid``.

.. code-block:: python

    kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3c',
          'utility': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}

To create and set the UUID attributes on a node, type:

.. code-block:: python

    nukeuuid.set(node, **kw)

To retrieve all nodes matching a specific UUID pattern, type:

.. code-block:: python

    kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3c',
          'utility': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}
    matched_nodes = nukeuuid.get_nodes(**kw)

.. _Full Documentation: http://nukeuuid.readthedocs.io/en/latest/
