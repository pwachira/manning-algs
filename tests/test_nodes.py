from trees.binary_node import BinaryNode
from trees.nary_node import NaryNode
import pytest


def test_binary():
    root = BinaryNode("Root")
    a = root.add_left(BinaryNode("A"))
    b = root.add_right(BinaryNode("B"))
    c = a.add_left(BinaryNode("C"))
    d = a.add_right(BinaryNode("D"))
    e = b.add_right(BinaryNode("E"))
    f = e.add_left(BinaryNode("F"))

    tree = root.__str__()
    print(tree)
    assert (
        tree
        == "Root:\n  A:\n    C:\n    D:\n  B:\n    None\n    E:\n      F:\n      None\n"
    )
    a_tree = a.__str__()
    print(a_tree)
    assert a_tree == "A:\n  C:\n  D:\n"


def test_nary():

    root = NaryNode("Root")
    [a, b, c] = [
        root.add_child(root_child)
        for root_child in [NaryNode("A"), NaryNode("B"), NaryNode("C")]
    ]
    [d, e] = [a.add_child(a_child) for a_child in [NaryNode("D"), NaryNode("E")]]
    f = c.add_child(NaryNode("F"))
    g = d.add_child(NaryNode("G"))
    [h, i] = [f.add_child(f_child) for f_child in [NaryNode("H"), NaryNode("I")]]

    tree = root.__str__()
    print(tree)
    assert (
        tree
        == "Root:\n  A:\n    D:\n      G:\n    E:\n  B:\n  C:\n    F:\n      H:\n      I:\n"
    )
    tree_a = a.__str__()
    assert tree_a == "A:\n  D:\n    G:\n  E:\n"
