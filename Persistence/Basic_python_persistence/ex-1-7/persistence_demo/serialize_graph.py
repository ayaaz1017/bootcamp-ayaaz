from persistence_demo.graph import Graph

def save_graph():
    graph = Graph()
    graph.add_node(1, "A")
    graph.add_node(2, "B")
    graph.add_edge(1, 2)

    json_string = graph.to_json()
    print("Serialized Graph:\n", json_string)

if __name__ == "__main__":
    save_graph()
