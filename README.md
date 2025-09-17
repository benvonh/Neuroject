# Neuroject
A simple Nix project to set up and run a Python GUI for drawing simple geometry.

## Features

- 🎨 Interactive GUI for drawing geometric shapes
- 📐 Support for circles, rectangles, lines, and triangles
- 🎨 Color picker for customizing shapes
- 📊 Built with tkinter and matplotlib
- 🏗️ Fully configured Nix development environment

## Quick Start

### Prerequisites

- [Nix](https://nixos.org/download.html) with flakes enabled

### Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/benvonh/Neuroject.git
   cd Neuroject
   ```

2. Run directly with Nix:
   ```bash
   nix run
   ```

### Development Environment

Enter the development shell for a full development environment:

```bash
nix develop
```

This provides:
- Python 3 with required packages (tkinter, matplotlib, numpy)
- Development tools (black, flake8)
- Direct access to run the application

Once in the development shell, you can:
- Run the application: `python src/main.py`
- Format code: `black src/`
- Lint code: `flake8 src/`

## Usage

The GUI provides intuitive controls for drawing:

1. **Shape Selection**: Choose from circle, rectangle, line, or triangle
2. **Color**: Click "Choose Color" to select drawing color
3. **Position**: Set X and Y coordinates for shape placement
4. **Size**: Adjust the size/radius of shapes
5. **Draw**: Click "Draw Shape" to add to canvas
6. **Clear**: Remove all shapes with "Clear All"

## Technical Details

- **GUI Framework**: tkinter (Python's built-in GUI library)
- **Plotting**: matplotlib for rendering geometric shapes
- **Mathematics**: numpy for geometric calculations
- **Package Management**: Nix flakes for reproducible builds

## Project Structure

```
Neuroject/
├── flake.nix          # Nix flake configuration
├── src/
│   └── main.py        # Main Python GUI application
├── README.md          # This file
├── LICENSE            # MIT License
└── .gitignore         # Git ignore patterns
```
