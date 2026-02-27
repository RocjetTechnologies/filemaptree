import os
from dataclasses import dataclass, field

@dataclass
class Node:
    name: str
    is_dir: bool
    children: list['Node'] = field(default_factory=list)


def walk(path: str, depth: int | None = None, ignore: set[str] | None = None) -> Node:
    ignore = ignore or set()
    
    root_name = os.path.basename(os.path.abspath(path)) or os.path.abspath(path)
    is_dir = os.path.isdir(path)
    
    root = Node(name=root_name, is_dir=is_dir, children=[])
    
    if not is_dir or depth == 0:
        return root
    
    _walk_recursive(path, root, current_depth=0, max_depth=depth, ignore=ignore)
    
    return root

def _walk_recursive(path: str, node: Node, current_depth: int, max_depth: int | None, ignore: set[str]) -> None:

    if max_depth is not None and current_depth >= max_depth:
        return
    
    try:
        entries = []
        with os.scandir(path) as scanner:
            for entry in scanner:
                if entry.name in ignore:
                    continue
                
                child = Node(
                    name=entry.name,
                    is_dir=entry.is_dir(follow_symlinks=False),
                    children=[]
                )
                entries.append((entry.path, child))
        
        entries.sort(key=lambda x: (not x[1].is_dir, x[1].name.lower()))
        
        for entry_path, child in entries:
            node.children.append(child)
            
            if child.is_dir:
                _walk_recursive(
                    entry_path, 
                    child, 
                    current_depth + 1, 
                    max_depth, 
                    ignore
                )
    
    except PermissionError:
        pass