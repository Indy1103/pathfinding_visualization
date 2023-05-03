import tkinter as tk


class GridCanvas(tk.Canvas):
    def __init__(self, parent, rows, columns, cell_size):
        # ... (implementation of GridCanvas class)

        super().__init__(parent, width = rows * cell_size, height = columns* cell_size, background="black")
        
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size

        self.draw_grid()
        self.draw_nodes()

    def draw_grid(self):
        for i in range(self.rows):
            self.create_line(i * self.cell_size, 0, i * self.cell_size, self.columns * self.cell_size)
        
        for j in range(self.columns):
            self.create_line(0, j * self.cell_size, self.rows * self.cell_size, j * self.cell_size)

    
    def draw_nodes(self):

        for i in range(self.rows - 1):
            for j in range(self.columns - 1):
                circle = self.create_oval(i * self.cell_size + self.cell_size - 15 ,
                                          j * self.cell_size + self.cell_size - 15 ,
                                          i * self.cell_size + self.cell_size + 15,
                                          j * self.cell_size + self.cell_size + 15,
                                          fill = "black", outline = "white")
                self.tag_bind(circle, '<Button-1>', self.toggle_node)
        

        

    def toggle_nodes(self):

        

        pass

        
        
class ControlPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # ... (create and configure UI elements within the ControlPanel)
        pass

    def on_start_button_click(self):
        # ... (handle the start button click event)
        pass
