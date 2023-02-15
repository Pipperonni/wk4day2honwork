


class Node:
    def __init__(self, value, nextnode=None):
        self.value = value
        self.nextnode = nextnode

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is None:
           self.head = node
           return 
        current_node = self.head
        while True:
            if current_node.nextnode is None:
                current_node.nextnode = node
                break
            current_node = current_node.nextnode

    def printlinkedlist(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.value, "->")
            currentnode = currentnode.nextnode
        print("None")
    
    def remove_node(self, value):
        node = Node(value)
        if self.head is None:
           self.head = node
           return 
        current_node = self.head
        while True:
            if current_node != node:
                current_node.nextnode = node
            else:
                current_node.nextnode = node.nextnode
                return
            current_node = node


            


tree = LinkedList()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

print(tree.printlinkedlist())

tree.remove_node(3)

print(tree.printlinkedlist())
