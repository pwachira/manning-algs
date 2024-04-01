from trees.binary_node import BinaryNode
from trees.nnary_node import NnaryNode
import pytest


def test_binary():
    root = BinaryNode("Root")
    a = root.add_left(BinaryNode("A"))
    b = root.add_right(BinaryNode("B"))
    c = a.add_left(BinaryNode("C"))
    d = a.add_right(BinaryNode("D"))
    e = b.add_right(BinaryNode("E"))
    f = e.add_left(BinaryNode("F"))
    for node in [root, a, b, c, d, e, f]:
        print(node)

    assert root.__str__() == "Root: A B"
    assert a.__str__() == "A: C D"
    assert b.__str__() == "B: None E"
    assert c.__str__() == "C: None None"
    assert d.__str__() == "D: None None"
    assert e.__str__() == "E: F None"
    assert f.__str__() == "F: None None"


def test_nnary():

    root = NnaryNode("Root")
    [a, b, c] = [
        root.add_child(root_child)
        for root_child in [NnaryNode("A"), NnaryNode("B"), NnaryNode("C")]
    ]
    [d, e] = [a.add_child(a_child) for a_child in [NnaryNode("D"), NnaryNode("E")]]
    f = c.add_child(NnaryNode("F"))
    g = d.add_child(NnaryNode("G"))
    [h, i] = [f.add_child(f_child) for f_child in [NnaryNode("H"), NnaryNode("I")]]

    for node in [root, a, b, c, d, e, f, g, h, i]:
        print(node)
    assert root.__str__() == "Root: A B C"
    assert a.__str__() == "A: D E"
    assert b.__str__() == "B: "
    assert c.__str__() == "C: F"
    assert d.__str__() == "D: G"
    assert e.__str__() == "E: "
    assert f.__str__() == "F: H I"
    assert g.__str__() == "G: "
    assert h.__str__() == "H: "
    assert i.__str__() == "I: "
