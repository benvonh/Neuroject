"""
Main GUI application for drawing simple geometry
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional, Tuple, List
import math


class DrawingCanvas:
    """Canvas widget for drawing lines and dots"""
    
    def __init__(self, parent):
        self.canvas = tk.Canvas(
            parent, 
            bg='white', 
            width=800, 
            height=600,
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Drawing state
        self.current_tool = "line"  # "line" or "dot"
        self.start_point: Optional[Tuple[int, int]] = None
        self.temp_line_id: Optional[int] = None
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        # Store drawn objects for potential future use
        self.drawn_objects: List[dict] = []
    
    def set_tool(self, tool: str):
        """Set the current drawing tool"""
        self.current_tool = tool
        # Cancel any ongoing line drawing
        if self.temp_line_id:
            self.canvas.delete(self.temp_line_id)
            self.temp_line_id = None
            self.start_point = None
    
    def on_click(self, event):
        """Handle mouse click events"""
        x, y = event.x, event.y
        
        if self.current_tool == "dot":
            self.draw_dot(x, y)
        elif self.current_tool == "line":
            if self.start_point is None:
                # Start of line
                self.start_point = (x, y)
                # Draw a temporary line to show preview
                self.temp_line_id = self.canvas.create_line(
                    x, y, x, y, 
                    fill="gray", 
                    width=2, 
                    tags="temp"
                )
    
    def on_drag(self, event):
        """Handle mouse drag events for line preview"""
        if self.current_tool == "line" and self.start_point and self.temp_line_id:
            x, y = event.x, event.y
            start_x, start_y = self.start_point
            # Update the temporary line
            self.canvas.coords(self.temp_line_id, start_x, start_y, x, y)
    
    def on_release(self, event):
        """Handle mouse release events"""
        if self.current_tool == "line" and self.start_point:
            x, y = event.x, event.y
            start_x, start_y = self.start_point
            
            # Remove temporary line
            if self.temp_line_id:
                self.canvas.delete(self.temp_line_id)
                self.temp_line_id = None
            
            # Draw the final line
            self.draw_line(start_x, start_y, x, y)
            self.start_point = None
    
    def draw_dot(self, x: int, y: int, radius: int = 3):
        """Draw a dot at the specified coordinates"""
        dot_id = self.canvas.create_oval(
            x - radius, y - radius, 
            x + radius, y + radius, 
            fill="blue", 
            outline="darkblue",
            width=1
        )
        
        # Store the dot information
        self.drawn_objects.append({
            "type": "dot",
            "x": x,
            "y": y,
            "radius": radius,
            "id": dot_id
        })
        
        return dot_id
    
    def draw_line(self, x1: int, y1: int, x2: int, y2: int):
        """Draw a line between two points"""
        line_id = self.canvas.create_line(
            x1, y1, x2, y2, 
            fill="red", 
            width=2,
            capstyle=tk.ROUND
        )
        
        # Store the line information
        self.drawn_objects.append({
            "type": "line",
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "id": line_id
        })
        
        return line_id
    
    def clear_canvas(self):
        """Clear all drawings from the canvas"""
        self.canvas.delete("all")
        self.drawn_objects.clear()
        self.start_point = None
        self.temp_line_id = None


class NeurojectGUI:
    """Main GUI application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Neuroject - Simple Geometry Drawing")
        self.root.geometry("900x700")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        # Create main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create toolbar
        toolbar = ttk.Frame(main_frame)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        # Tool selection
        ttk.Label(toolbar, text="Tool:").pack(side=tk.LEFT, padx=(0, 5))
        
        self.tool_var = tk.StringVar(value="line")
        tool_frame = ttk.Frame(toolbar)
        tool_frame.pack(side=tk.LEFT, padx=(0, 20))
        
        ttk.Radiobutton(
            tool_frame, 
            text="Line", 
            variable=self.tool_var, 
            value="line",
            command=self.on_tool_change
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Radiobutton(
            tool_frame, 
            text="Dot", 
            variable=self.tool_var, 
            value="dot",
            command=self.on_tool_change
        ).pack(side=tk.LEFT)
        
        # Buttons
        ttk.Button(
            toolbar, 
            text="Clear", 
            command=self.clear_canvas
        ).pack(side=tk.LEFT, padx=(20, 10))
        
        ttk.Button(
            toolbar, 
            text="About", 
            command=self.show_about
        ).pack(side=tk.RIGHT)
        
        # Create drawing canvas
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.drawing_canvas = DrawingCanvas(canvas_frame)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready - Select a tool and start drawing")
        status_bar = ttk.Label(
            main_frame, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN
        )
        status_bar.pack(fill=tk.X, pady=(10, 0))
    
    def on_tool_change(self):
        """Handle tool selection change"""
        tool = self.tool_var.get()
        self.drawing_canvas.set_tool(tool)
        
        if tool == "line":
            self.status_var.set("Line tool selected - Click and drag to draw lines")
        elif tool == "dot":
            self.status_var.set("Dot tool selected - Click to place dots")
    
    def clear_canvas(self):
        """Clear the drawing canvas"""
        result = messagebox.askyesno(
            "Clear Canvas", 
            "Are you sure you want to clear all drawings?"
        )
        if result:
            self.drawing_canvas.clear_canvas()
            self.status_var.set("Canvas cleared - Ready to draw")
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About Neuroject",
            "Neuroject v0.1.0\n\n"
            "Simple GUI for drawing geometry\n"
            "- Use Line tool to draw lines\n"
            "- Use Dot tool to place dots\n"
            "- Click Clear to reset canvas\n\n"
            "Built with Python and Nix"
        )


def main():
    """Main entry point"""
    root = tk.Tk()
    app = NeurojectGUI(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        print(f"Error running application: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())