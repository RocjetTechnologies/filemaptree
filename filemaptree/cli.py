import argparse
import os
import sys

from .walker import walk
from .renderer import render


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="filemaptree",
        description="Render a deterministic ASCII file tree",
        add_help=True
    )
    
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Directory path to render (default: current directory)"
    )
    
    parser.add_argument(
        "--depth",
        type=int,
        metavar="N",
        help="Maximum depth to traverse (unlimited if omitted)"
    )
    
    parser.add_argument(
        "--ignore",
        type=str,
        metavar="NAMES",
        help="Comma-separated list of exact names to ignore"
    )
    
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: path does not exist: {args.path}", file=sys.stderr)
        sys.exit(1)
    
    ignore_set = set()
    if args.ignore:
        ignore_set = set(name.strip() for name in args.ignore.split(",") if name.strip())

    try:
        tree = walk(args.path, depth=args.depth, ignore=ignore_set)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    output = render(tree)
    print(output)
