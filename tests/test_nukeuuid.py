# nukeuuid tests
import pytest


def test_set_single(nuke, nukeuuid, uuid):
    node = nuke.nodes.Shuffle(name='Shuffle')
    kw = {'': ''}
    nukeuuid.set_uuid(node, **kw)

    assert nukeuuid._has_attr(node, 'uuid')
    assert uuid.UUID(node['uuid'].value())


def test_set_uuid(nuke, nukeuuid):
    nodes = [node for node in
             [nuke.nodes.Write(name='Write_{0}'.format(i)) for i in range(3)]]
    kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3c',
          'utility': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}
    nukeuuid.set_uuid(nodes, **kw)

    for node in nodes:
        assert nukeuuid._has_attr(node, 'uuid')
        assert nukeuuid._has_attr(node, 'utility_uuid')
        assert node['uuid'].value() == \
            'fca7201e-b53d-4918-9ab0-bb4ec5590f3c'
        assert node['utility_uuid'].value() == \
            '5f2d525d-3e00-4bc5-88c4-794ad87f5699'


def test_get(nuke, nukeuuid):
    kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3c',
          'utility': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}
    nodes = nukeuuid.get_nodes(**kw)
    assert len(nodes) == 3


def test_get_invalid_uuid(nuke, nukeuuid):
    with pytest.raises(nukeuuid.NukeUUIDError):
        kw = {'': 'fca7201e-b53d-4918-9ab0-bb4ec5590f3x'}
        nukeuuid.get_nodes(**kw)


def test_get_invalid_attr(nuke, nukeuuid):
    with pytest.raises(nukeuuid.NukeUUIDError):
        kw = {'utility2': '5f2d525d-3e00-4bc5-88c4-794ad87f5699'}
        nukeuuid.get_nodes(**kw)
