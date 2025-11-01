class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next


if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(20)

    # print(node1.get_data())
    # print(node1.get_next())

    node1.set_data(30)
    node1.set_next(node2)

    print(node1.get_data())
    print(node1.get_next())
    