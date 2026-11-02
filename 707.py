"""
LeetCode 707: Design Linked List

Question:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the
current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate
the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
- MyLinkedList(): Initializes the MyLinkedList object.
- int get(int index): Get the value of the indexth node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val): Add a node of value val before the first element of the linked list.
  After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val): Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val): Add a node of value val before the indexth node in the linked list.
  If index equals the length of the linked list, the node will be appended to the end of the linked list.
  If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index): Delete the indexth node in the linked list, if the index is valid.

Given Constraints:
- 0 <= index, val <= 1000
- Please do not use the built-in LinkedList library.
- At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex, and deleteAtIndex.

Example 1:
Input:
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output:
[null, null, null, null, 2, null, 3]

Explanation:
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""

from typing import List, Optional


class ListNode:
    """Node definition for a doubly linked list."""

    def __init__(
        self,
        val: int = 0,
        prev: Optional["ListNode"] = None,
        next: Optional["ListNode"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    """
    Doubly Linked List Implementation with Sentinel (Dummy) Head and Tail nodes.

    Advantages:
    - Sentinel nodes eliminate edge cases for insertions and deletions at boundaries.
    - Bidirectional links allow traversal from either the head or tail, cutting
      worst-case search operations in half (O(min(index, size - index))).
    - O(1) time complexity for head and tail additions.
    """

    def __init__(self):
        """Initializes the empty linked list with dummy head and tail."""
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        Time Complexity: O(min(index, size - index))
        """
        if index < 0 or index >= self.size:
            return -1

        # Optimize traversal direction: search from closest end
        if index < self.size - index:
            curr = self.head.next
            for _ in range(index):
                assert curr is not None
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                assert curr is not None
                curr = curr.prev

        assert curr is not None
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        Time Complexity: O(1)
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element of the linked list.
        Time Complexity: O(1)
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        - If index == length of list, append to the end.
        - If index > length of list, do not insert.
        - If index < 0, insert at the head.
        Time Complexity: O(min(index, size - index))
        """
        if index > self.size:
            return

        if index < 0:
            index = 0

        # Find predecessor (pred) and successor (succ)
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                assert pred is not None
                pred = pred.next
            assert pred is not None
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                assert succ is not None
                succ = succ.prev
            assert succ is not None
            pred = succ.prev

        assert pred is not None and succ is not None
        new_node = ListNode(val, prev=pred, next=succ)
        pred.next = new_node
        succ.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        Time Complexity: O(min(index, size - index))
        """
        if index < 0 or index >= self.size:
            return

        # Find predecessor (pred) and successor (succ) of node to delete
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                assert pred is not None
                pred = pred.next
            assert pred is not None and pred.next is not None
            to_delete = pred.next
            succ = to_delete.next
        else:
            succ = self.tail
            for _ in range(self.size - 1 - index):
                assert succ is not None
                succ = succ.prev
            assert succ is not None and succ.prev is not None
            to_delete = succ.prev
            pred = to_delete.prev

        assert pred is not None and succ is not None
        pred.next = succ
        succ.prev = pred

        self.size -= 1

    def to_list(self) -> List[int]:
        """Utility method to return all node values as a Python list."""
        result = []
        curr = self.head.next
        while curr is not None and curr is not self.tail:
            result.append(curr.val)
            curr = curr.next
        return result

    def __repr__(self) -> str:
        return " -> ".join(map(str, self.to_list())) if self.size > 0 else "Empty"


if __name__ == "__main__":
    print("Testing LeetCode 707: Design Linked List\n" + "=" * 50)

    # Test Case 1: LeetCode Example 1
    llist = MyLinkedList()
    operations = [
        ("addAtHead", [1]),
        ("addAtTail", [3]),
        ("addAtIndex", [1, 2]),
        ("get", [1]),
        ("deleteAtIndex", [1]),
        ("get", [1]),
    ]
    expected_outputs = [None, None, None, 2, None, 3]

    print("Executing Example 1:")
    for (op, args), expected in zip(operations, expected_outputs):
        method = getattr(llist, op)
        result = method(*args)
        print(f"  {op}{tuple(args)} => Result: {result}, Expected: {expected}, State: {llist.to_list()}")
        assert result == expected, f"Failed on {op}{tuple(args)}: expected {expected}, got {result}"

    print("-" * 50)

    # Test Case 2: Boundary and Edge Cases
    print("Executing Edge Cases:")
    llist2 = MyLinkedList()

    # Get from empty list
    assert llist2.get(0) == -1
    print("  get(0) on empty list: -1 -> PASS")

    # Delete from empty list
    llist2.deleteAtIndex(0)
    assert llist2.to_list() == []
    print("  deleteAtIndex(0) on empty list: no error -> PASS")

    # Add at index out of bounds
    llist2.addAtIndex(5, 100)
    assert llist2.to_list() == []
    print("  addAtIndex(5, 100) when empty: no insertion -> PASS")

    # Add at head and tail
    llist2.addAtHead(10)
    llist2.addAtTail(20)
    llist2.addAtHead(5)
    # List is now [5, 10, 20]
    assert llist2.to_list() == [5, 10, 20]
    print(f"  addAtHead/Tail sequence -> {llist2.to_list()} -> PASS")

    # Delete head
    llist2.deleteAtIndex(0)
    assert llist2.to_list() == [10, 20]
    print(f"  delete head (index 0) -> {llist2.to_list()} -> PASS")

    # Delete tail
    llist2.deleteAtIndex(1)
    assert llist2.to_list() == [10]
    print(f"  delete tail (index 1) -> {llist2.to_list()} -> PASS")

    # Delete the only remaining element
    llist2.deleteAtIndex(0)
    assert llist2.to_list() == []
    print(f"  delete sole remaining element -> {llist2.to_list()} -> PASS")

    print("=" * 50)
    print("All tests passed successfully!")

