"""ASCII tree rendering."""

from .walker import Node


def render(root: Node) -> str:
    """
    Render a Node tree as ASCII.
    
    Args:
        root: Root node to render
        
    Returns:
        ASCII tree representation
    """
    lines = [root.name]
    _render_children(root.children, "", lines)
    return "\n".join(lines)


def _render_children(children: list[Node], prefix: str, lines: list[str]) -> None:
    """
    Recursively render children with proper ASCII connectors.
    
    Args:
        children: List of child nodes to render
        prefix: Current line prefix for indentation
        lines: Accumulator for output lines
    """
    for i, child in enumerate(children):
        is_last = i == len(children) - 1
        
        # Choose connector based on position
        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + child.name)
        
        # Recurse into children with updated prefix
        if child.children:
            # Extension for the next level
            extension = "    " if is_last else "│   "
            _render_children(child.children, prefix + extension, lines)
