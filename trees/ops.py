from trees.binary_node import BinaryNode
from trees.nary_node import NaryNode

NOT_FOUND = "Value {} not found"
FOUND = "Found {}"


class BinaryOps:
    def find_value(self, node: BinaryNode, value: str) -> str:
        fmt_found = FOUND.format(value)
        fmt_not_found = NOT_FOUND.format(value)
        if not node:
            return
        if node.value == value:
            return fmt_found
        lft = self.find_value(node.left, value)
        right = self.find_value(node.right, value)
        if lft == fmt_found or right == fmt_found:
            return fmt_found
        else:
            return fmt_not_found


class NaryOps:
    def find_value(self, node: NaryNode, value: str) -> str:
        fmt_found = FOUND.format(value)
        fmt_not_found = NOT_FOUND.format(value)
        if not node:
            return
        if node.value == value:
            return fmt_found
        res = []
        for child in node.children:
            res.append(self.find_value(child, value))
        if fmt_found in res:
            return fmt_found
        else:
            return fmt_not_found
