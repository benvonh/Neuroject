# Neuroject

Simple Python GUI for drawing geometry using tkinter.

## Description

A minimal Nix project that provides a simple GUI window for drawing lines and dots on a canvas. Built with Python and managed entirely through Nix.

## Usage

### Running the application

```bash
# Run directly with Nix
nix run

# Or enter development environment and run manually
nix develop
python main.py
```

### Development

```bash
# Enter the development shell
nix develop

# The shell provides Python with tkinter support
python main.py
```

## Features

- **Line tool**: Click and drag to draw lines
- **Dot tool**: Click to place dots
- **Clear button**: Reset the canvas
- **Simple interface**: Minimal, easy-to-use GUI

## Requirements

- Nix with flakes enabled
- No additional dependencies needed (handled by Nix)

## License

MIT License - see [LICENSE](LICENSE) file for details.
