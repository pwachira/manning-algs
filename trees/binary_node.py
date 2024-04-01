class BinaryNode:
    def __init__(self, value: str) -> None:
        self.value = value
        self.right: BinaryNode = None
        self.left: BinaryNode = None

    def __str__(self) -> str:
        left = self.left.value if self.left is not None else None
        right = self.right.value if self.right is not None else None
        return f"{self.value}: {left} {right}"

    def add_left(self, node: "BinaryNode") -> "BinaryNode":
        self.left = node
        return self.left

    def add_right(self, node: "BinaryNode") -> "BinaryNode":
        self.right = node
        return self.right
