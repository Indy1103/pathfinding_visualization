import tkinter as tk


class GridCanvas(tk.Canvas):
    def __init__(self, parent, rows, columns, cell_size):
        # ... (implementation of GridCanvas class)

        super().__init__(parent, width = rows * cell_size, height = columns* cell_size, background="black")
        
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.mouse_moved = False

        self.draw_grid()
        self.draw_nodes()
        

    def draw_grid(self):
        for i in range(self.rows):
            self.create_line(i * self.cell_size, 0, i * self.cell_size, self.columns * self.cell_size,fill= "#444444")
        
        for j in range(self.columns):
            self.create_line(0, j * self.cell_size, self.rows * self.cell_size, j * self.cell_size, fill= "#444444")

    
    def draw_nodes(self):
        
        #Create Circles
        for i in range(self.rows - 1):
            for j in range(self.columns - 1):
                circle = self.create_oval(i * self.cell_size + self.cell_size - 15 ,
                                          j * self.cell_size + self.cell_size - 15 ,
                                          i * self.cell_size + self.cell_size + 15,
                                          j * self.cell_size + self.cell_size + 15,
                                          fill = "black", outline = "black")
                
                self.tag_bind(circle, '<ButtonPress-1>', self.on_node_press)
                self.tag_bind(circle, '<ButtonRelease-1>', self.on_node_release)
        

    def on_node_press(self, event):
        self.mouse_moved = False
        self.start_node_id = self.find_closest(event.x, event.y)
        self.start_cords = self.coords(self.start_node_id)
        self.start_cords = (float((self.start_cords[0]+ ((self.start_cords[2]- self.start_cords[0])/2))), 
                            float((self.start_cords[1]+((self.start_cords[3]- self.start_cords[1])/2))))

        print("Start Cords: ", self.start_cords)

    def on_node_release(self, event):
        end_node_id = self.find_closest(event.x, event.y)
        end_cords = self.coords(end_node_id)
        end_cords = (float((end_cords[0]+(end_cords[2]- end_cords[0])/2)), 
                     float((end_cords[1]+(end_cords[3]- end_cords[1])/2)))
        print(self.start_cords ," , ", end_cords)
        
        if self.start_node_id == end_node_id:
            
            self.toggle_nodes(event)

        else:
            self.add_edges(self.start_cords, end_cords)
            

        
    def toggle_nodes(self, event):

        circle_color = self.itemcget(self.find_closest(event.x, event.y), 'fill')

        new_color = 'white' if circle_color == 'black' else 'black'
                                     
        self.itemconfig(self.find_closest(event.x, event.y), fill= new_color)
        
    def add_edges(self, start_node, end_node):
        
        edge = self.create_line(start_node, end_node, fill="white")
    
               
        
class ControlPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # ... (create and configure UI elements within the ControlPanel)
        pass

    def on_start_button_click(self):
        # ... (handle the start button click event)
        pass
