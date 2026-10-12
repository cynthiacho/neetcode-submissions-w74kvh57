# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        arr, cur = [], head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        n = len(arr)
        k %= n
        cur = head
        for i in range(n - k, n):
            cur.val = arr[i]
            cur = cur.next

        for i in range(n - k):
            cur.val = arr[i]
            cur = cur.next

        return head