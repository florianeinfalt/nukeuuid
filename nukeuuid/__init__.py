import os
import re
import sys
import uuid
import platform

try:
    os.environ['NON_PRODUCTION_CONTEXT']
except:
    if platform.system() == 'Darwin':
        application = r'Nuke\d+\.\d+v\d+.app'
    elif platform.system() == 'Windows':
        application = r'Nuke\d+\.\d+.exe'
    else:
        raise RuntimeError('OS {0} is not supported'.format(platform.system()))
    match = re.search(application, sys.executable)
    if not match:
        raise RuntimeError('Import nukeuuid from within Nuke')
    import nuke

__version__ = '0.1.1'
__all__ = []


class NukeUUIDError(ValueError):
    """
    Exception indicating an error related to UUIDs,
    inherits from :class:`ValueError`.
    """
    def __init__(self, message):
        super(NukeUUIDError, self).__init__(message)


def _convert_type(type_):
    """
    Given a ``type_``, convert to a UUID attribute name.
    The empty string converts to ``uuid``.

    :param type_: UUID type
    :type type_: str
    :return: UUID attribute name
    :rtype: str
    """
    if type_ == 'uuid' or type_ == '':
        return 'uuid'
    else:
        return '{0}_uuid'.format(type_)


def _has_attr(node, attr):
    """
    Given a ``node`` and an ``attr``, check if the ``attr`` exists on the
    ``node``.

    :param node: Node
    :type node: :class:`~nuke.Node`
    :param attr: UUID attribute
    :type attr: str
    """
    if attr in node.knobs():
        return True
    return False


def _make_attr(node, attr):
    """
    Given a ``node`` and an ``attr``, create ``attr`` on ``node`` if ``attr``
    does not exist on ``node``. The new attribute is a
    :class:`~nuke.Text_Knob`.

    :param node: Node
    :type node: :class:`~nuke.Node`
    :param attr: UUID attribute
    :type attr: str
    """
    if not _has_attr(node, attr):
        node.addKnob(nuke.Text_Knob(attr, attr))


def set(nodes, **kwargs):
    """
    Given a list of ``nodes`` and a set of keyword arguments ``kwargs``,
    set UUID(s) on ``nodes``.

    :param nodes: Nodes
    :type nodes: list
    :param \**kwargs: UUID dictionary

    Usage:

    >>> import nukeuuid
    >>> kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3c',
              'utility': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}
    >>> nukeuuid.set(nuke.selectedNodes(), **kw)
    """
    if not isinstance(nodes, list):
        nodes = [nodes]
    for node in nodes:
        for type_, uuid_ in kwargs.iteritems():
            if not type_ and not uuid_:
                uuid_ = str(uuid.uuid1())
            attr = _convert_type(type_)
            _make_attr(node, attr)
            node[attr].setValue(uuid_)
            node[attr].setEnabled(False)


def get_nodes(**kwargs):
    """
    Given a set of keyword arguments ``kwargs``, get all nodes that match the
    UUID pattern. Raise :class:`~nukeuuid.NukeUUIDError` if no nodes were
    matched.

    :param \**kwargs: UUID dictionary

    Usage:

    >>> import nukeuuid
    >>> kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3c',
              'utility': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}
    >>> nodes = nukeuuid.get_nodes(**kw)
    """
    nodes = []
    for node in nuke.allNodes():
        try:
            for type_, uuid_ in kwargs.iteritems():
                try:
                    if node[_convert_type(type_)].value() != uuid_:
                        raise NukeUUIDError('UUID not matched'.format(type_))
                except NameError:
                    raise NukeUUIDError('No attr named {0}'.format(type_))
            nodes.append(node)
        except NukeUUIDError:
            continue
    if not nodes:
        raise NukeUUIDError('No nodes were matched')
    return nodes
