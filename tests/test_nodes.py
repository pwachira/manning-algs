from trees.binary_node import BinaryNode
from trees.nary_node import NaryNode
from trees.ops import BinaryOps, NaryOps
import pytest


@pytest.fixture(scope="session")
def binary_tree() -> BinaryNode:
    root = BinaryNode("Root")
    a = root.add_left(BinaryNode("A"))
    b = root.add_right(BinaryNode("B"))
    a.add_left(BinaryNode("C"))
    a.add_right(BinaryNode("D"))
    e = b.add_right(BinaryNode("E"))
    e.add_left(BinaryNode("F"))
    return root


@pytest.fixture(scope="session")
def binary_node_b(binary_tree) -> BinaryNode:
    return binary_tree.right


@pytest.fixture(scope="session")
def binary_ops() -> BinaryOps:
    return BinaryOps()


@pytest.fixture(scope="session")
def nary_ops() -> NaryOps:
    return NaryOps()


@pytest.fixture(scope="session")
def nary_tree() -> NaryNode:
    root = NaryNode("Root")
    [a, _, c] = [
        root.add_child(root_child)
        for root_child in [NaryNode("A"), NaryNode("B"), NaryNode("C")]
    ]
    [d, _] = [a.add_child(a_child) for a_child in [NaryNode("D"), NaryNode("E")]]
    f = c.add_child(NaryNode("F"))
    d.add_child(NaryNode("G"))
    [f.add_child(f_child) for f_child in [NaryNode("H"), NaryNode("I")]]
    return root


@pytest.fixture(scope="session")
def nary_node_c(nary_tree) -> NaryNode:
    return nary_tree.children[2]


def test_binary(binary_tree):
    root: BinaryNode = binary_tree
    assert (
        root.__str__()
        == "Root:\n  A:\n    C:\n    D:\n  B:\n    None\n    E:\n      F:\n      None\n"  # noqa
    )
    a_tree = root.left
    assert a_tree.__str__() == "A:\n  C:\n  D:\n"


def test_nary(nary_tree):

    tree = nary_tree
    assert (
        tree.__str__()
        == "Root:\n  A:\n    D:\n      G:\n    E:\n  B:\n  C:\n    F:\n      H:\n      I:\n"  # noqa
    )
    tree_a = tree.children[0]
    assert tree_a.__str__() == "A:\n  D:\n    G:\n  E:\n"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Root", "Found Root"),
        ("E", "Found E"),
        ("F", "Found F"),
        ("Q", "Value Q not found"),
    ],
)
def test_find_value_from_root(
    binary_ops: BinaryOps, binary_tree: BinaryNode, value: str, expected: str
):
    assert binary_ops.find_value(binary_tree, value) == expected


def test_find_value_from_binary_non_root(
    binary_ops: BinaryOps, binary_node_b: BinaryNode
):
    assert binary_ops.find_value(binary_node_b, "F") == "Found F"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Root", "Found Root"),
        ("E", "Found E"),
        ("F", "Found F"),
        ("Q", "Value Q not found"),
    ],
)
def test_find_value_from_nary_root(
    nary_ops: NaryOps, nary_tree: NaryNode, value: str, expected: str
):
    assert nary_ops.find_value(nary_tree, value) == expected


def test_find_value_from_non_nary_root(nary_ops: NaryOps, nary_node_c: BinaryNode):
    assert nary_ops.find_value(nary_node_c, "F") == "Found F"
