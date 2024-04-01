class NnaryNode:
    def __init__(self, val: str) -> None:
        self.value = val
        self.children: list[NnaryNode] = []

    def __str__(self) -> str:
        children = " ".join([node.value for node in self.children])
        return f"{self.value}: {children}"

    def add_child(self, node: "NnaryNode") -> "NnaryNode":
        self.children.append(node)
        return node
