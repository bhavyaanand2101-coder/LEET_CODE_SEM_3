"""
LeetCode 206: Reverse Linked List

Question:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Given:
- head: Optional[ListNode] (the head node of a singly linked list)
- Constraints:
    - The number of nodes in the list is in the range [0, 5000].
    - -5000 <= Node.val <= 5000

Output:
- Optional[ListNode]: The head node of the reversed linked list.

Examples:
- Example 1:
    Input: head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

- Example 2:
    Input: head = [1, 2]
    Output: [2, 1]

- Example 3:
    Input: head = []
    Output: []

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        values = []
        curr = self
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        return " -> ".join(values)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Default LeetCode entry point: delegates to the iterative approach (O(1) extra space).
        """
        return self.reverseListIterative(head)

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative Approach:
        Use two pointers (`prev` and `curr`) to reverse the direction of links in place.

        Steps:
        1. Initialize `prev = None` and `curr = head`.
        2. While `curr` is not None:
           a. Store the next node (`next_node = curr.next`).
           b. Reverse the current node's pointer (`curr.next = prev`).
           c. Advance `prev` to `curr`.
           d. Advance `curr` to `next_node`.
        3. At the end of the loop, `prev` will be pointing to the new head of the reversed list.

        Time Complexity: O(n) - We traverse each node exactly once.
        Space Complexity: O(1) - Only a few pointers are used.
        """
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head

        while curr is not None:
            next_node: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive Approach:
        Reverse the rest of the list recursively and fix the head node's link on the way back.

        Base Case:
        - If `head` is None or `head.next` is None, the list is either empty or contains
          a single element, which is already reversed. Return `head`.

        Recursive Step:
        - Call `reverseListRecursive(head.next)` which reverses the sublist and returns
          the new head of the reversed list (`new_head`).
        - Make the original next node point back to `head`: `head.next.next = head`.
        - Set `head.next = None` to break the old forward link (preventing a cycle).
        - Return `new_head`.

        Time Complexity: O(n) - Each node is visited once.
        Space Complexity: O(n) - Due to recursion call stack for n frames.
        """
        # Base case
        if head is None or head.next is None:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)

        # Fix the pointers:
        # head.next is the node immediately following head in the original list.
        # Setting head.next.next = head makes that node point back to head.
        head.next.next = head
        head.next = None

        return new_head


# Helper functions to convert between Python lists and Linked Lists
def list_to_linked_list(elements: List[int]) -> Optional[ListNode]:
    """Converts a Python list to a singly linked list."""
    if not elements:
        return None
    head = ListNode(elements[0])
    curr = head
    for val in elements[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a singly linked list to a Python list."""
    elements = []
    curr = head
    while curr:
        elements.append(curr.val)
        curr = curr.next
    return elements


if __name__ == "__main__":
    solution = Solution()

    # Test cases with Given Inputs and Expected Outputs
    test_cases = [
        {
            "input": [1, 2, 3, 4, 5],
            "expected": [5, 4, 3, 2, 1],
        },
        {
            "input": [1, 2],
            "expected": [2, 1],
        },
        {
            "input": [],
            "expected": [],
        },
        {
            "input": [42],
            "expected": [42],
        },
        {
            "input": [-1, -2, -3],
            "expected": [-3, -2, -1],
        },
    ]

    print("Running Tests for LeetCode 206: Reverse Linked List\n" + "=" * 50)

    for i, test in enumerate(test_cases, 1):
        input_data = test["input"]
        expected = test["expected"]

        # Test Iterative Approach
        llist_iter = list_to_linked_list(input_data)
        reversed_iter = solution.reverseListIterative(llist_iter)
        result_iter = linked_list_to_list(reversed_iter)

        # Test Recursive Approach
        llist_rec = list_to_linked_list(input_data)
        reversed_rec = solution.reverseListRecursive(llist_rec)
        result_rec = linked_list_to_list(reversed_rec)
        print(f"Test Case {i}:")
        print(f"  Input:     {input_data}")
        print(f"  Expected:  {expected}")
        print(f"  Iterative: {result_iter} -> {'PASS' if result_iter == expected else 'FAIL'}")
        print(f"  Recursive: {result_rec} -> {'PASS' if result_rec == expected else 'FAIL'}")
        print("-" * 50)
        assert result_iter == expected, f"Iterative failed for {input_data}: got {result_iter}, expected {expected}"
        assert result_rec == expected, f"Recursive failed for {input_data}: got {result_rec}, expected {expected}"
    print("All test cases passed successfully!")