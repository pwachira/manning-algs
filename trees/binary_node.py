class BinaryNode:

    INDENT = "  "

    def __init__(self, value: str) -> None:
        self._value = value
        self.right: BinaryNode = None
        self.left: BinaryNode = None

    @property
    def value(self):
        return self._value

    def __str__(self, level: int = 0) -> str:
        return self.recurse(node=self, level=level)

    def recurse(self, node: "BinaryNode", level=0) -> str:
        if not node:
            none_str = f"{level * BinaryNode.INDENT}None\n"
            return none_str
        curr_str = f"{level * BinaryNode.INDENT}{node.value}:\n"
        left_str = f"{self.recurse(node.left, level=level+1)}"
        right_str = f"{self.recurse(node.right, level=level+1)}"
        if not node.left and not node.right:
            children_str = curr_str
        else:
            children_str = f"{curr_str}{left_str}{right_str}"
        return children_str

    def add_left(self, node: "BinaryNode") -> "BinaryNode":
        self.left = node
        return self.left

    def add_right(self, node: "BinaryNode") -> "BinaryNode":
        self.right = node
        return self.right
