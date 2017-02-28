Getting Started
===============

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

To create and set the UUID attributes on a node (or a list of nodes), type:

.. code-block:: python

    nukeuuid.set(node, **kw)

To retrieve all nodes matching a specific UUID pattern, type:

.. code-block:: python

    kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3c',
          'utility': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}
    matched_nodes = nukeuuid.get_nodes(**kw)
