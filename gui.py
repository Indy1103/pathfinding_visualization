import tkinter as tk
from algorithms.dfs import dfs
from algorithms.bfs import bfs

class GridCanvas(tk.Canvas):
    def __init__(self, parent, rows, columns, cell_size):
        # ... (implementation of GridCanvas class)

        super().__init__(parent, width = rows * cell_size, height = columns* cell_size, background="black")
        
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.mouse_moved = False

        self.starting_node = None
        self.draw_grid()
        self.draw_nodes()
        
        self.node_edge = {}
        self.adjacency_list = {}
        self.bind('<KeyPress-s>', self.toggle_start_node)
        self.focus_set()
        

        

    def draw_grid(self):
        for i in range(self.rows):
            self.create_line(i * self.cell_size, 0, i * self.cell_size, self.columns * self.cell_size,fill= "#444444")
        
        for j in range(self.columns):
            self.create_line(0, j * self.cell_size, self.rows * self.cell_size, j * self.cell_size, fill= "#444444")
    
    def draw_nodes(self):
        
        #Create Circles
        for i in range(self.rows - 1):
            for j in range(self.columns - 1):
                self.circle = self.create_oval(i * self.cell_size + self.cell_size - 15 ,
                                          j * self.cell_size + self.cell_size - 15 ,
                                          i * self.cell_size + self.cell_size + 15,
                                          j * self.cell_size + self.cell_size + 15,
                                          fill = "black", outline = "black", tags = 'node')
                
                self.tag_bind(self.circle, '<ButtonPress-1>', self.on_node_press)
                self.tag_bind(self.circle, '<ButtonRelease-1>', self.on_node_release)
                
        
    def on_node_press(self, event):
        self.mouse_moved = False
        self.start_node_id = (self.find_closest(event.x, event.y))
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
            print(node_1_status)
            
            node_2_status = self.itemcget(end_node_id, 'fill')
            print(node_2_status)

            if node_1_status == ('white' or 'orange') and node_2_status ==('white' or 'orange'):
                
                self.add_edges(self.start_cords, end_cords, self.start_node_id, end_node_id)          
       
    def toggle_nodes(self, event):

        circle_color = self.itemcget(self.find_closest(event.x, event.y), 'fill')

        new_color = 'white' if circle_color == 'black' else 'black'

        if new_color == 'white':

            self.itemconfig(self.find_closest(event.x, event.y), fill= new_color)
            print(self.start_node_id)
            self.node_edge[self.start_node_id] = []
            self.adjacency_list[int(self.start_node_id[0])] = set()
            
        elif new_color == 'black':
            
            # cycle through the edges. Delete any edges. \
            self.itemconfig(self.find_closest(event.x, event.y), fill= new_color)
            for edge_id in self.node_edge[self.start_node_id]:

                self.delete(edge_id)
            
            self.node_edge.pop(self.start_node_id)
            self.adjacency_list.pop(int(self.start_node_id[0]))

                       
    def add_edges(self, start_node, end_node, start_node_id, end_node_id):
        
        self.edge = self.create_line(start_node, end_node, fill="white", tags= 'edge')

        self.node_edge[start_node_id].append(self.edge)
        self.node_edge[end_node_id].append(self.edge)

        self.adjacency_list[int(start_node_id[0])].add(int(end_node_id[0]))
        self.adjacency_list[int(end_node_id[0])].add(int(start_node_id[0]))
    
    def toggle_start_node(self, event):

        x, y = self.winfo_pointerx() - self.winfo_rootx(), self.winfo_pointery() - self.winfo_rooty()
        self.node = self.find_closest(x, y)
        self.node = self.find_closest(event.x, event.y)        
        self.colour = self.itemcget( self.node , 'fill')
        
        if self.colour == 'white' and self.starting_node:
            self.prev_start_node = self.starting_node
            self.starting_node = self.node

            self.itemconfig(self.prev_start_node, fill= 'white')
            self.itemconfig(self.starting_node, fill= 'orange')

        if self.colour == 'white':

            self.starting_node = self.node
            self.itemconfig(self.starting_node, fill= 'orange')
    

    def toggle_clear(self):

        self.starting_node = None
        self.delete("node")  # Delete all nodes
        self.delete("edge")  # Delete all edges
        self.draw_grid()
        self.draw_nodes()

        self.node_edge = {}
        self.adjacency_list = {}

        print("Clear Toggled")

    def visualize_path(self, visited_nodes):
        for index, node in enumerate(visited_nodes):
            self.after(index * 500, self.color_node, node, "blue")

    def color_node(self, node_id, color):
        self.itemconfig(node_id, fill=color)       


        
class ControlPanel(tk.Frame):
    def __init__(self, parent, grid_canvas):
        super().__init__(parent)

        self.grid_canvas = grid_canvas
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

        algorithm = self.selected_algorithm.get()
        graph = self.grid_canvas.adjacency_list
        
        print(graph)

        starting_node = int(self.grid_canvas.starting_node[0])
        print(starting_node)

        def update_visualization(node_id):
            self.grid_canvas.color_node(node_id, "blue")
            self.grid_canvas.update_idletasks()
            self.grid_canvas.after(500)

        if algorithm == "DFS":
            result = dfs(graph, starting_node, callback=update_visualization)
        elif algorithm == "BFS":
            result = bfs(graph, starting_node, callback=update_visualization)

        for node in graph:
            self.grid_canvas.color_node(node, "white")
        

        print("Start button clicked. Selected algorithm:", self.selected_algorithm.get(), "Result", result)

    def on_clear_button_click(self):
        
        self.grid_canvas.toggle_clear()
        print("Clear button clicked")

