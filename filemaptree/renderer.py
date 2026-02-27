from .walker import Node

def render(root: Node) -> str:

    lines = [root.name]
    _render_children(root.children, "", lines)
    return "\n".join(lines)


def _render_children(children: list[Node], prefix: str, lines: list[str]) -> None:

    for i, child in enumerate(children):
        is_last = i == len(children) - 1
        
        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + child.name)
        
        if child.children:
            extension = "    " if is_last else "│   "
            _render_children(child.children, prefix + extension, lines)
