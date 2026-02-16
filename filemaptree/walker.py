"""Directory traversal and tree construction."""

import os
from dataclasses import dataclass, field


@dataclass
class Node:
    """Represents a file or directory in the tree."""
    name: str
    is_dir: bool
    children: list['Node'] = field(default_factory=list)


def walk(path: str, depth: int | None = None, ignore: set[str] | None = None) -> Node:
    """
    Walk a directory and build a tree structure.
    
    Args:
        path: Root path to walk
        depth: Maximum depth to traverse (None = unlimited)
        ignore: Set of exact names to ignore
        
    Returns:
        Root Node with children populated
    """
    ignore = ignore or set()
    
    # Get the root name
    root_name = os.path.basename(os.path.abspath(path)) or os.path.abspath(path)
    is_dir = os.path.isdir(path)
    
    root = Node(name=root_name, is_dir=is_dir, children=[])
    
    # If it's a file or depth is 0, return immediately
    if not is_dir or depth == 0:
        return root
    
    # Build the tree recursively
    _walk_recursive(path, root, current_depth=0, max_depth=depth, ignore=ignore)
    
    return root


def _walk_recursive(path: str, node: Node, current_depth: int, max_depth: int | None, ignore: set[str]) -> None:
    """
    Recursively populate a node's children.
    
    Args:
        path: Current directory path
        node: Current node to populate
        current_depth: Current depth level (0 = root level)
        max_depth: Maximum depth to traverse (None = unlimited)
        ignore: Set of exact names to ignore
    """
    # Check if we've reached max depth
    if max_depth is not None and current_depth >= max_depth:
        return
    
    try:
        entries = []
        with os.scandir(path) as scanner:
            for entry in scanner:
                # Skip ignored names
                if entry.name in ignore:
                    continue
                
                child = Node(
                    name=entry.name,
                    is_dir=entry.is_dir(follow_symlinks=False),
                    children=[]
                )
                entries.append((entry.path, child))
        
        # Sort: directories first, then alphabetically (case-insensitive)
        entries.sort(key=lambda x: (not x[1].is_dir, x[1].name.lower()))
        
        # Add sorted children to node
        for entry_path, child in entries:
            node.children.append(child)
            
            # Recurse into directories
            if child.is_dir:
                _walk_recursive(
                    entry_path, 
                    child, 
                    current_depth + 1, 
                    max_depth, 
                    ignore
                )
    
    except PermissionError:
        # Skip directories we can't read
        pass
