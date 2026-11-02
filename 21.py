"""
LeetCode 21: Merge Two Sorted Lists

Question:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Given:
- list1: Optional[ListNode] (head of first sorted linked list)
- list2: Optional[ListNode] (head of second sorted linked list)
- Constraints:
    - The number of nodes in both lists is in the range [0, 50].
    - -100 <= Node.val <= 100
    - Both list1 and list2 are sorted in non-decreasing order.

Output:
- Optional[ListNode]: The head of the merged sorted linked list.

Examples:
- Example 1:
    Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
    Output: [1, 1, 2, 3, 4, 4]

- Example 2:
    Input: list1 = [], list2 = []
    Output: []

- Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Default LeetCode entry point: delegates to the iterative approach (O(1) extra space).
        """
        return self.mergeTwoListsIterative(list1, list2)

    def mergeTwoListsIterative(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Iterative Approach using a Dummy (Sentinel) Node:

        Steps:
        1. Create a dummy head node to simplify edge cases (avoids special-casing the merged head).
        2. Maintain a `tail` pointer pointing to the current end of the merged list.
        3. Compare the current nodes of list1 and list2:
           - Splice the smaller node to `tail.next`.
           - Advance the pointer of the chosen list.
           - Advance `tail = tail.next`.
        4. Once one list is exhausted, attach the remaining non-empty list directly to `tail.next`.
        5. Return `dummy.next`.

        Time Complexity: O(n + m) - Each node from both lists is visited once.
        Space Complexity: O(1) - Only a few pointer references; nodes are spliced in-place.
        """
        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining nodes of whichever list is not empty
        tail.next = list1 if list1 is not None else list2

        return dummy.next

    def mergeTwoListsRecursive(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Recursive Approach:

        Base Cases:
        - If `list1` is None, return `list2`.
        - If `list2` is None, return `list1`.

        Recursive Step:
        - Determine which list has the smaller value at its head.
        - Recursively merge the remainder of that list with the other list.
        - Set the chosen head's `next` pointer to the result of the recursive call.
        - Return the chosen head node.

        Time Complexity: O(n + m) - Total number of recursive calls is equal to n + m.
        Space Complexity: O(n + m) - Recursion call stack memory.
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2


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
            "list1": [1, 2, 4],
            "list2": [1, 3, 4],
            "expected": [1, 1, 2, 3, 4, 4],
            "description": "Standard example with equal and interleaved elements",
        },
        {
            "list1": [],
            "list2": [],
            "expected": [],
            "description": "Both lists are empty",
        },
        {
            "list1": [],
            "list2": [0],
            "expected": [0],
            "description": "One list empty, one list with single element",
        },
        {
            "list1": [5],
            "list2": [1, 2, 3, 4],
            "expected": [1, 2, 3, 4, 5],
            "description": "Different lengths: one element vs multiple elements",
        },
        {
            "list1": [1, 2, 3],
            "list2": [4, 5, 6],
            "expected": [1, 2, 3, 4, 5, 6],
            "description": "Completely disjoint ranges",
        },
        {
            "list1": [-10, -5, 0],
            "list2": [-7, -3, 2],
            "expected": [-10, -7, -5, -3, 0, 2],
            "description": "Lists with negative values",
        },
    ]

    print("Running Tests for LeetCode 21: Merge Two Sorted Lists\n" + "=" * 60)

    for i, test in enumerate(test_cases, 1):
        l1_data = test["list1"]
        l2_data = test["list2"]
        expected = test["expected"]
        desc = test["description"]

        # Test Iterative Approach (re-create lists to avoid shared mutation)
        l1_iter = list_to_linked_list(l1_data)
        l2_iter = list_to_linked_list(l2_data)
        merged_iter = solution.mergeTwoListsIterative(l1_iter, l2_iter)
        result_iter = linked_list_to_list(merged_iter)

        # Test Recursive Approach
        l1_rec = list_to_linked_list(l1_data)
        l2_rec = list_to_linked_list(l2_data)
        merged_rec = solution.mergeTwoListsRecursive(l1_rec, l2_rec)
        result_rec = linked_list_to_list(merged_rec)

        print(f"Test Case {i} ({desc}):")
        print(f"  list1:     {l1_data}")
        print(f"  list2:     {l2_data}")
        print(f"  Expected:  {expected}")
        print(f"  Iterative: {result_iter} -> {'PASS' if result_iter == expected else 'FAIL'}")
        print(f"  Recursive: {result_rec} -> {'PASS' if result_rec == expected else 'FAIL'}")
        print("-" * 60)

        assert result_iter == expected, f"Iterative failed for {l1_data}, {l2_data}: got {result_iter}, expected {expected}"
        assert result_rec == expected, f"Recursive failed for {l1_data}, {l2_data}: got {result_rec}, expected {expected}"

    print("All test cases passed successfully!")

