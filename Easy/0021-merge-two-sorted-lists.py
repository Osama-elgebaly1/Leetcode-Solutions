# Definition for singly-linked list.
# This is the structure used for each node in the linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val        # The value of the current node
        self.next = next      # Pointer to the next node in the list

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merges two sorted linked lists into one sorted linked list.
        This function keeps the original nodes and links them in sorted order.

        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()     # A dummy node to start the merged list
        current = dummy        # Pointer to build the merged list

        # Loop while both lists have elements
        while list1 and list2:
            if list1.val <= list2.val:
                current.next  = list1  # Attach the smaller node to the result
                list1 = list1.next     # Move to the next node in list1
            else:
                current.next = list2   # Attach the smaller node to the result
                list2 = list2.next     # Move to the next node in list2

            current = current.next     # Move the current pointer forward

        # At least one of the lists is now empty.
        # Directly connect the remaining non-empty list (if any)
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the merged list (skipping the dummy node)
        return dummy.next
