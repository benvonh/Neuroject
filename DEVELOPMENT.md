# Neuroject Development

## Development Setup

This project uses Nix flakes for reproducible development environments.

### Quick Development Workflow

1. Enter the development shell:
   ```bash
   nix develop
   ```

2. Run the application:
   ```bash
   python src/main.py
   ```

3. Format code:
   ```bash
   black src/
   ```

4. Lint code:
   ```bash
   flake8 src/
   ```

### Project Components

- **flake.nix**: Nix flake configuration with all dependencies
- **src/main.py**: Main Python GUI application
- **run-example.sh**: Example usage script

### Dependencies

The Nix environment provides:
- Python 3 with tkinter (GUI framework)
- matplotlib (for plotting geometric shapes)
- numpy (for mathematical calculations)
- black (code formatter)
- flake8 (code linter)

### GUI Features

The application provides:
- Shape drawing (circles, rectangles, lines, triangles)
- Color selection
- Interactive parameter controls
- Real-time canvas updates
- Clear functionality