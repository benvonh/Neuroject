# Neuroject
Simple GUI for drawing geometry - lines and dots

A Python application with Nix support for creating simple geometric drawings using an intuitive graphical interface.

## Features

- **Drawing Tools**:
  - Line tool: Click and drag to draw lines
  - Dot tool: Click to place dots/points
- **Interactive Canvas**: 800x600 pixel drawing area
- **Clear Function**: Reset canvas to start fresh
- **Cross-platform**: Works on Linux, macOS, and Windows

## Requirements

- Python 3.8+
- tkinter (usually included with Python)
- Nix (optional, for reproducible environment)

## Installation & Usage

### Using Nix (Recommended)

1. **Enter development shell**:
   ```bash
   nix develop
   ```

2. **Run the application**:
   ```bash
   python -m neuroject
   ```

### Using Python directly

1. **Install dependencies**:
   ```bash
   # On Ubuntu/Debian
   sudo apt install python3-tk
   
   # On macOS (with Homebrew)
   brew install python-tk
   
   # On Windows, tkinter is usually included
   ```

2. **Install the package**:
   ```bash
   pip install -e .
   ```

3. **Run the application**:
   ```bash
   neuroject
   # or
   python -m neuroject.main
   ```

## How to Use

1. **Select a tool**:
   - Click "Line" to draw lines
   - Click "Dot" to place dots

2. **Draw**:
   - **Line tool**: Click and drag from start to end point
   - **Dot tool**: Single click to place a dot

3. **Clear canvas**: Click "Clear" button to reset

## Development

### Project Structure
```
neuroject/
├── src/neuroject/
│   ├── __init__.py      # Package initialization
│   └── main.py          # Main GUI application
├── flake.nix            # Nix flake configuration
├── pyproject.toml       # Python project configuration
└── README.md           # This file
```

### Testing

Run the test suite:
```bash
python test_gui.py
```

### Creating a Demo
```bash
python demo_gui.py
```

## License

MIT License - see [LICENSE](LICENSE) file for details.
