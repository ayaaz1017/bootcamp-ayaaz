from cyclic_demo.node import Node, serialize_nodes

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")

node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node1)  # Creates a cycle

serialize_nodes("cyclic_nodes.pkl", node1)
print("Cyclic Nodes serialized successfully.")
