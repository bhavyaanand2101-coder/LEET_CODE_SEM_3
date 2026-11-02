# Define the building block (Node) of the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Stores the value
        self.next = None  # Points to the next node

# Define the Linked List structure
class LinkedList:
    def __init__(self):
        self.head = None  # The list starts empty

    # Method to add data to the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to search for a value in the list
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True  # Found the number!
            current = current.next
        return False  # Number is not in the list

# --- Main Program Execution ---

# 1. Create the Linked List
llist = LinkedList()

# 2. Enter the data: 2, 6, 9, 4
llist.append(2)
llist.append(6)
llist.append(9)
llist.append(4)

# 3. Check if 9 is present
target_value = 9
if llist.search(target_value):
    print(f"Yes, {target_value} is present in the linked list.")
else:
    print(f"No, {target_value} is not present in the linked list.")
