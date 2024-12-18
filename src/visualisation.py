import os
import networkx as nx
import matplotlib.pyplot as plt

class ArgumentationSystem:
    def __init__(self, filepath):
        self.filepath = filepath
        self.graph = nx.DiGraph()
        self.load_arguments_and_attacks()

    def load_arguments_and_attacks(self):
        """Loads arguments and attacks from the file and creates a graph."""
        with open(self.filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("arg"):
                    # Clean argument to remove parentheses and trailing spaces
                    argument = line.split('(')[1].split(')')[0].strip()  # Remove parentheses
                    self.graph.add_node(argument)
                elif line.startswith("att"):
                    # Clean attacks to remove parentheses and trailing spaces
                    parts = line.split('(')[1].split(')')[0].split(',')
                    attacker = parts[0].strip()  # Remove trailing spaces
                    target = parts[1].strip()  # Remove trailing spaces
                    self.graph.add_edge(attacker, target)

    def visualize(self):
        """Displays the argumentation system graphically."""
        pos = nx.spring_layout(self.graph)  # Node disposition
        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold", arrows=True)
        plt.title(f"Argumentation System - {os.path.basename(self.filepath)}")
        plt.savefig(f"../outputs/plots/{os.path.basename(self.filepath)}.png")
        plt.show()

def visualize_all_systems(directory):
    """Loads and visualises all argumentation systems in a directory."""
    # List all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".apx"):
            filepath = os.path.join(directory, filename)
            print(f"Visualisation de {filename}...")
            system = ArgumentationSystem(filepath)
            system.visualize()

# Example of use
if __name__ == "__main__":
    visualize_all_systems("../tests")

