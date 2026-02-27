# filemaptree

Deterministic ASCII file tree renderer.

## Purpose

`filemaptree` renders a deterministic ASCII file tree. It is a single-purpose tool designed for clean, stable, and reusable directory visualization.

## Features

- **Deterministic ordering**: Directories first, then files, both alphabetically (case-insensitive)
- **Depth control**: Limit tree depth with `--depth N`
- **Ignore patterns**: Skip specific directory/file names with `--ignore`
- **ASCII rendering**: Clean tree structure using `├──`, `└──`, `│`
- **Cross-platform**: Stable output across Linux, macOS, Windows

## Installation

```bash
pip install filemaptree
```

## Usage

### Basic usage

```bash
filemaptree
```

Or current directory,

```bash
filemaptree .
```

## Output example

```
filemaptree
│   ├── __init__.py
│   ├── cli.py
│   ├── main.py
│   ├── renderer.py
│   └── walker.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

### Specific path

```bash
filemaptree /path/to/directory
```

### Depth control

Show only root:

```bash
filemaptree --depth 0
```

Show root + immediate children:

```bash
filemaptree --depth 1
```

Show root + two levels:

```bash
filemaptree --depth 2
```

### Ignore patterns

Ignore specific names:

```bash
filemaptree --ignore __pycache__,node_modules,.git
```

### Combined options

```bash
filemaptree /path/to/directory --depth 3 --ignore .git,node_modules
```

## Architecture

```
filemaptree/
├── __init__.py    # Package marker
├── main.py        # Entry point
├── cli.py         # Argument parsing and orchestration
├── walker.py      # Directory traversal and tree building
└── renderer.py    # ASCII tree rendering
```

## License

MIT

## Author
[Caleb Wodi](https://github.com/calchiwo)