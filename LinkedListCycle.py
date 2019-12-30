# Definition for singly-linked list.
import pdb
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        d = {}
        
        while head.next is not None:
            #pdb.set_trace()
            if d.get(id(head)):
                return True
            else:
                d[id(head)] = 1
                head = head.next

        return False

head = ListNode(3)
head.next = ListNode(-4)
head.next.next = ListNode(-4)
head.next.next.next = ListNode(-4)
#head.next.next.next.next = head.next

test = Solution()
print(test.hasCycle(head))