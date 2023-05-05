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


        self.node_edge = {}


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


    def on_node_release(self, event):
        end_node_id = self.find_closest(event.x, event.y)
        end_cords = self.coords(end_node_id)
        end_cords = (float((end_cords[0]+(end_cords[2]- end_cords[0])/2)), 
                     float((end_cords[1]+(end_cords[3]- end_cords[1])/2)))
                
        if self.start_node_id == end_node_id:
            
            self.toggle_nodes(event)

        else:
            node_1_status = self.itemcget(self.start_node_id, 'fill')
            node_2_status = self.itemcget(end_node_id, 'fill')

            if node_1_status == 'white' and node_2_status =='white':

                self.add_edges(self.start_cords, end_cords, self.start_node_id, end_node_id)
            

        
    def toggle_nodes(self, event):

        circle_color = self.itemcget(self.find_closest(event.x, event.y), 'fill')

        new_color = 'white' if circle_color == 'black' else 'black'

        if new_color == 'white':

            self.itemconfig(self.find_closest(event.x, event.y), fill= new_color)
            self.node_edge[self.start_node_id] = []
            

        elif new_color == 'black':
            
            # cycle through the edges. Delete any edges. \
            self.itemconfig(self.find_closest(event.x, event.y), fill= new_color)
            for edge_id in self.node_edge[self.start_node_id]:

                self.delete(edge_id)
            
            self.node_edge.pop(self.start_node_id)
                   
    
    def add_edges(self, start_node, end_node, start_node_id, end_node_id):
        
        edge = self.create_line(start_node, end_node, fill="white", tags= 'edge')

        self.node_edge[start_node_id].append(edge)
        self.node_edge[end_node_id].append(edge)
    
    def delete_edges(self):
        
        self.find_closest()
        
        pass


        
class ControlPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.algorithm_label = tk.Label(self, text="Algorithm:")
        self.algorithm_label.pack(side="left")

        self.algorithms = ["DFS", "BFS"]
        self.selected_algorithm = tk.StringVar(self)
        self.selected_algorithm.set(self.algorithms[0])

        self.algorithm_dropdown = tk.OptionMenu(self, self.selected_algorithm, *self.algorithms)
        self.algorithm_dropdown.pack(side="left")

        self.start_button = tk.Button(self, text="Start", command=self.on_start_button_click)
        self.start_button.pack(side="left")

        self.clear_button = tk.Button(self, text="Clear", command=self.on_clear_button_click)
        self.clear_button.pack(side="left")

    def on_start_button_click(self):
        # Handle the start button click event here
        print("Start button clicked. Selected algorithm:", self.selected_algorithm.get())

    def on_clear_button_click(self):
        # Handle the clear button click event here
        print("Clear button clicked")
