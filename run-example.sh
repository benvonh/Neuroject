#!/usr/bin/env bash
# Example usage script for Neuroject
# This demonstrates the various ways to run the application

set -e

echo "Neuroject - Python GUI Geometry Drawer"
echo "======================================"
echo

# Check if nix is available
if command -v nix &> /dev/null; then
    echo "✓ Nix is available"
    
    echo
    echo "Available commands:"
    echo "1. nix run                    - Run the packaged application"
    echo "2. nix develop                - Enter development environment"
    echo "3. nix develop -c python src/main.py - Run directly in nix environment"
    echo
    
    echo "To run the application:"
    echo "  nix run"
    echo
    echo "To enter development mode:"
    echo "  nix develop"
    echo "  # Then inside the shell:"
    echo "  python src/main.py"
    
else
    echo "✗ Nix is not available"
    echo
    echo "Please install Nix to use this project:"
    echo "  curl -L https://nixos.org/nix/install | sh"
    echo
    echo "Make sure flakes are enabled by adding to ~/.config/nix/nix.conf:"
    echo "  experimental-features = nix-command flakes"
fi

echo
echo "Project structure:"
find . -type f -name "*.nix" -o -name "*.py" -o -name "*.md" | grep -v ".git" | sort