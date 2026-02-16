# filemaptree

Deterministic ASCII file tree renderer.

## Version

0.1.0

## Purpose

`filemaptree` renders a deterministic ASCII file tree. It is a single-purpose tool designed for clean, stable, and reusable directory visualization.

## Installation

```bash
pip install -e .
```

## Usage

### Basic usage

```bash
# Current directory
python -m filemaptree.main .

# Specific path
python -m filemaptree.main /path/to/directory
```

### Depth control

```bash
# Show only root
python -m filemaptree.main . --depth 0

# Show root + immediate children
python -m filemaptree.main . --depth 1

# Show root + two levels
python -m filemaptree.main . --depth 2
```

### Ignore patterns

```bash
# Ignore specific names (exact match)
python -m filemaptree.main . --ignore __pycache__,node_modules,.git
```

### Combined options

```bash
python -m filemaptree.main /path/to/repo --depth 3 --ignore .git,node_modules
```

## Features

- **Deterministic ordering**: Directories first, then files, both alphabetically (case-insensitive)
- **Depth control**: Limit tree depth with `--depth N`
- **Ignore patterns**: Skip specific directory/file names with `--ignore`
- **ASCII rendering**: Clean tree structure using `├──`, `└──`, `│`
- **Cross-platform**: Stable output across operating systems

## Architecture

```
filemaptree/
├── __init__.py    # Package marker
├── main.py        # Entry point
├── cli.py         # Argument parsing and orchestration
├── walker.py      # Directory traversal and tree building
└── renderer.py    # ASCII tree rendering
```

### Separation of concerns

- **cli.py**: Parses arguments, validates paths, orchestrates flow
- **walker.py**: Traverses filesystem, applies filters, builds Node tree
- **renderer.py**: Converts Node tree to ASCII output

## Output example

```
filemaptree
├── __init__.py
├── cli.py
├── main.py
├── renderer.py
└── walker.py
```

## Design principles

- Single-purpose tool
- Minimal and precise
- No feature creep
- Deterministic output
- Clean separation of concerns
- Production-ready code

MIT

## Author
[Caleb Wodi](https://github.com/calchiwo)