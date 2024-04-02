class NaryNode:
    INDENT = "  "

    def __init__(self, val: str) -> None:
        self.value = val
        self.children: list[NaryNode] = []

    def __str__(self, level: int = 0) -> str:
        return self.recurse(node=self, level=level)

    def recurse(self, node: "NaryNode", level: int) -> str | None:
        if not node:
            return
        curr_str = f"{NaryNode.INDENT * level}{node.value}:\n"
        children_str = ""
        for child_node in node.children:
            child_str = self.recurse(node=child_node, level=level + 1)
            children_str = f"{children_str}{child_str}"
        return f"{curr_str}{children_str}"

    def add_child(self, node: "NaryNode") -> "NaryNode":
        self.children.append(node)
        return node
