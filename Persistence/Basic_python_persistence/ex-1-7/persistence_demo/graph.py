import json

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id, value):
        self.nodes[node_id] = value

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def to_json(self):
        """Custom serialization logic."""
        return json.dumps({"nodes": self.nodes, "edges": self.edges}, indent=4)
