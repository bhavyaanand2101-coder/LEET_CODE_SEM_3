"""
LeetCode 876: Middle of the Linked List

Question:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Given:
- head: Optional[ListNode] (the head node of a singly linked list)
- Constraints:
    - The number of nodes in the list is in the range [1, 100].
    - 1 <= Node.val <= 100

Output:
- Optional[ListNode]: The middle node (and the rest of the list following it).

Examples:
- Example 1:
    Input: head = [1, 2, 3, 4, 5]
    Output: [3, 4, 5]
    Explanation: The middle node of the list is node 3.

- Example 2:
    Input: head = [1, 2, 3, 4, 5, 6]
    Output: [4, 5, 6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Fast & Slow Pointer Approach (Tortoise and Hare Algorithm):
        Maintain two pointers:
        - `slow`: moves one node at a time.
        - `fast`: moves two nodes at a time.

        When `fast` reaches the end of the list (either `fast` is None or `fast.next` is None),
        `slow` will be located precisely at the middle node (or second middle node for even length).

        Trace:
        - Odd length ([1, 2, 3, 4, 5]):
            Start: slow=1, fast=1
            Step 1: slow=2, fast=3
            Step 2: slow=3, fast=5 (fast.next is None -> stop)
            Returns node 3.

        - Even length ([1, 2, 3, 4, 5, 6]):
            Start: slow=1, fast=1
            Step 1: slow=2, fast=3
            Step 2: slow=3, fast=5
            Step 3: slow=4, fast=None (fast is None -> stop)
            Returns node 4 (second middle node).

        Time Complexity: O(n) - Single pass traversal.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def middleNodeTwoPass(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Alternative Two-Pass Approach:
        1. First pass: Count the total number of nodes (n).
        2. Second pass: Advance n // 2 steps from head to reach the middle node.

        Time Complexity: O(n) - Two passes.
        Space Complexity: O(1) - Constant auxiliary space.
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        middle_index = length // 2
        curr = head
        for _ in range(middle_index):
            assert curr is not None
            curr = curr.next

        return curr


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

    # Test cases with inputs and expected output lists
    test_cases = [
        {
            "input": [1, 2, 3, 4, 5],
            "expected": [3, 4, 5],
            "description": "Odd number of elements (5 nodes)",
        },
        {
            "input": [1, 2, 3, 4, 5, 6],
            "expected": [4, 5, 6],
            "description": "Even number of elements (6 nodes)",
        },
        {
            "input": [1],
            "expected": [1],
            "description": "Single element list",
        },
        {
            "input": [1, 2],
            "expected": [2],
            "description": "Two element list",
        },
        {
            "input": [7, 8, 9, 10, 11, 12, 13],
            "expected": [10, 11, 12, 13],
            "description": "Odd number of elements (7 nodes)",
        },
    ]

    print("Running Tests for LeetCode 876: Middle of the Linked List\n" + "=" * 60)

    for i, test in enumerate(test_cases, 1):
        input_data = test["input"]
        expected = test["expected"]
        desc = test["description"]

        # Test Fast & Slow Pointer Approach
        llist_fast_slow = list_to_linked_list(input_data)
        mid_node_fast_slow = solution.middleNode(llist_fast_slow)
        result_fast_slow = linked_list_to_list(mid_node_fast_slow)

        # Test Two-Pass Approach
        llist_two_pass = list_to_linked_list(input_data)
        mid_node_two_pass = solution.middleNodeTwoPass(llist_two_pass)
        result_two_pass = linked_list_to_list(mid_node_two_pass)

        print(f"Test Case {i} ({desc}):")
        print(f"  Input:            {input_data}")
        print(f"  Expected:         {expected}")
        print(f"  Fast & Slow:      {result_fast_slow} -> {'PASS' if result_fast_slow == expected else 'FAIL'}")
        print(f"  Two-Pass:         {result_two_pass} -> {'PASS' if result_two_pass == expected else 'FAIL'}")
        print("-" * 60)

        assert result_fast_slow == expected, f"Fast & slow failed for {input_data}: got {result_fast_slow}, expected {expected}"
        assert result_two_pass == expected, f"Two-pass failed for {input_data}: got {result_two_pass}, expected {expected}"

    print("All test cases passed successfully!")

