from cyclic_demo.node import deserialize_nodes

node = deserialize_nodes("cyclic_nodes.pkl")
print("Deserialized Node:", node)
print("Next Node:", node.next)
print("Cycle Check:", node.next.next.next == node)  # Should be True
