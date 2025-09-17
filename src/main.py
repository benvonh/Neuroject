#!/usr/bin/env python3
"""
Neuroject - Simple Python GUI for drawing geometric shapes.

This application provides a simple interface to draw basic geometric shapes
like circles, rectangles, and lines using tkinter and matplotlib.
"""

import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


class GeometryDrawer:
    """Main application class for the geometry drawing GUI."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Neuroject - Geometry Drawer")
        self.root.geometry("800x600")
        
        # Initialize matplotlib figure
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid(True, alpha=0.3)
        self.ax.set_aspect('equal')
        
        # Current drawing color
        self.current_color = 'blue'
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Control panel
        control_frame = ttk.LabelFrame(main_frame, text="Drawing Controls", padding=10)
        control_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))
        
        # Shape selection
        ttk.Label(control_frame, text="Shape:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.shape_var = tk.StringVar(value="circle")
        shape_combo = ttk.Combobox(control_frame, textvariable=self.shape_var, 
                                  values=["circle", "rectangle", "line", "triangle"])
        shape_combo.grid(row=0, column=1, padx=5)
        shape_combo.state(['readonly'])
        
        # Color selection
        ttk.Label(control_frame, text="Color:").grid(row=0, column=2, sticky=tk.W, padx=(10, 5))
        self.color_button = tk.Button(control_frame, text="Choose Color", 
                                     command=self.choose_color, bg=self.current_color,
                                     width=12)
        self.color_button.grid(row=0, column=3, padx=5)
        
        # Draw button
        draw_button = ttk.Button(control_frame, text="Draw Shape", command=self.draw_shape)
        draw_button.grid(row=0, column=4, padx=10)
        
        # Clear button
        clear_button = ttk.Button(control_frame, text="Clear All", command=self.clear_canvas)
        clear_button.grid(row=0, column=5, padx=5)
        
        # Parameters frame
        params_frame = ttk.LabelFrame(main_frame, text="Parameters", padding=10)
        params_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))
        
        # X coordinate
        ttk.Label(params_frame, text="X:").grid(row=0, column=0, sticky=tk.W)
        self.x_var = tk.DoubleVar(value=0.0)
        x_spin = ttk.Spinbox(params_frame, from_=-10.0, to=10.0, increment=0.5, 
                            textvariable=self.x_var, width=8)
        x_spin.grid(row=0, column=1, padx=5)
        
        # Y coordinate
        ttk.Label(params_frame, text="Y:").grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
        self.y_var = tk.DoubleVar(value=0.0)
        y_spin = ttk.Spinbox(params_frame, from_=-10.0, to=10.0, increment=0.5, 
                            textvariable=self.y_var, width=8)
        y_spin.grid(row=0, column=3, padx=5)
        
        # Size/Radius
        ttk.Label(params_frame, text="Size:").grid(row=0, column=4, sticky=tk.W, padx=(10, 0))
        self.size_var = tk.DoubleVar(value=2.0)
        size_spin = ttk.Spinbox(params_frame, from_=0.1, to=10.0, increment=0.1, 
                               textvariable=self.size_var, width=8)
        size_spin.grid(row=0, column=5, padx=5)
        
        # Canvas frame
        canvas_frame = ttk.LabelFrame(main_frame, text="Drawing Canvas", padding=5)
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Matplotlib canvas
        self.canvas = FigureCanvasTkAgg(self.fig, canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to draw")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
    def choose_color(self):
        """Open color chooser dialog."""
        color = colorchooser.askcolor(title="Choose drawing color")
        if color[1]:  # If a color was selected
            self.current_color = color[1]
            self.color_button.config(bg=self.current_color)
            
    def draw_shape(self):
        """Draw the selected shape with current parameters."""
        try:
            shape = self.shape_var.get()
            x = self.x_var.get()
            y = self.y_var.get()
            size = self.size_var.get()
            
            if shape == "circle":
                self.draw_circle(x, y, size)
            elif shape == "rectangle":
                self.draw_rectangle(x, y, size)
            elif shape == "line":
                self.draw_line(x, y, size)
            elif shape == "triangle":
                self.draw_triangle(x, y, size)
                
            self.canvas.draw()
            self.status_var.set(f"Drew {shape} at ({x:.1f}, {y:.1f})")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to draw shape: {str(e)}")
            self.status_var.set("Error drawing shape")
            
    def draw_circle(self, x, y, radius):
        """Draw a circle."""
        circle = plt.Circle((x, y), radius, fill=False, 
                          edgecolor=self.current_color, linewidth=2)
        self.ax.add_patch(circle)
        
    def draw_rectangle(self, x, y, size):
        """Draw a rectangle."""
        # Rectangle centered at (x, y) with width and height = size
        rect = plt.Rectangle((x - size/2, y - size/2), size, size, 
                           fill=False, edgecolor=self.current_color, linewidth=2)
        self.ax.add_patch(rect)
        
    def draw_line(self, x, y, length):
        """Draw a line."""
        # Draw a horizontal line centered at (x, y)
        x_start, x_end = x - length/2, x + length/2
        self.ax.plot([x_start, x_end], [y, y], 
                    color=self.current_color, linewidth=2)
        
    def draw_triangle(self, x, y, size):
        """Draw an equilateral triangle."""
        # Create triangle vertices
        height = size * np.sqrt(3) / 2
        vertices = np.array([
            [x, y + height/2],           # Top vertex
            [x - size/2, y - height/2],  # Bottom left
            [x + size/2, y - height/2],  # Bottom right
            [x, y + height/2]            # Close the triangle
        ])
        
        self.ax.plot(vertices[:, 0], vertices[:, 1], 
                    color=self.current_color, linewidth=2)
        
    def clear_canvas(self):
        """Clear all drawn shapes."""
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid(True, alpha=0.3)
        self.ax.set_aspect('equal')
        self.canvas.draw()
        self.status_var.set("Canvas cleared")


def main():
    """Main function to run the application."""
    # Create the main window
    root = tk.Tk()
    
    # Create and run the application
    app = GeometryDrawer(root)
    
    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()