
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_At_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at last
    def insert_At_Last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
list1 = Linked_list()

list1.insert_At_beg(10)
list1.insert_At_beg(20)
list1.insert_At_beg(30)

list1.insert_At_Last(90)
list1.insert_At_Last(100)

list1.display()
