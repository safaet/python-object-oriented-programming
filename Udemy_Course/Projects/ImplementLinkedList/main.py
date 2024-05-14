from node import Node

node_2 = Node(3)
node_1 = Node(5, node_2)

# node_1 -> node_2

print(node_1.next is node_2)