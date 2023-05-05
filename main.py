import tkinter as tk
from gui import GridCanvas, ControlPanel

def main():
    # Create the top-level window (main container)
    root = tk.Tk()

    # Create instances of the custom classes, specifying the parent widget
    grid_canvas = GridCanvas(root, rows=10, columns=10, cell_size=70)
    control_panel = ControlPanel(root)

    # Add the custom widgets to the top-level window's layout
    grid_canvas.pack(side=tk.LEFT)
    control_panel.pack(side=tk.RIGHT)

    

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()



