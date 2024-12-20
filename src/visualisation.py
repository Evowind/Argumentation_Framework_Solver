import os
import networkx as nx
import matplotlib.pyplot as plt

#Basically, it pulls data from a file and builds a graph out of it.
class ArgumentationSystem:
    def __init__(self, filepath):
        #Filepath stored, empty graph set up.
        self.filepath = filepath
        self.graph = nx.DiGraph()
        self.load_arguments_and_attacks()  #Let’s load the data!

    def load_arguments_and_attacks(self):
        """Loads args and attacks from file, makes the graph."""
        with open(self.filepath, 'r') as file:
            for line in file:
                line = line.strip()  #Clean up spaces
                if line.startswith("arg"):  #Found an argument
                    arg = line.split('(')[1].split(')')[0].strip()  #Grab what's inside ()
                    self.graph.add_node(arg)  #Add node to graph
                elif line.startswith("att"):  #Found an attack
                    parts = line.split('(')[1].split(')')[0].split(',')
                    attacker = parts[0].strip()  #First is attacker
                    target = parts[1].strip()  #Second is target
                    self.graph.add_edge(attacker, target)  #Link them in graph

    def visualize(self):
        """Draws the argument system graphically."""
        pos = nx.spring_layout(self.graph)  #Place nodes nicely
        plt.figure(figsize=(8, 6))  #Decent size
        #Draw the graph, make it look good, hoepfully
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color="lightblue", 
                font_size=12, font_weight="bold", arrows=True)
        #Title based on filename
        plt.title(f"Argument System - {os.path.basename(self.filepath)}")
        #Save the image (better have the folder sorted first!)
        plt.savefig(f"../outputs/plots/{os.path.basename(self.filepath)}.png")
        plt.show()  #Ta-da!

#Goes through a folder and visualises every system it finds.
def visualize_all_systems(directory):
    """Looks in dir, shows all argument systems."""
    # Check all files in the dir
    for filename in os.listdir(directory):
        if filename.endswith(".apx"):  #Only care about .apx files
            filepath = os.path.join(directory, filename)
            print(f"Visualising {filename}...")  #Heads up to the user
            system = ArgumentationSystem(filepath)  #Load the system
            system.visualize()  #Show it off

#Entry point, runs the lot.
if __name__ == "__main__":
    visualize_all_systems("tests") #Change "tests" if necessary