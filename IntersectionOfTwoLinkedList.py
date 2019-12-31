#Definition for singly-linked list.
import pdb
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = {}
        i = 1
        #pdb.set_trace()
        while headA is not None:
            d[id(headA)] = i
            i += 1
            headA = headA.next
        #pdb.set_trace()
        while headB is not None:
            try:
                if d[id(headB)]:
                    return headB
            except:
                headB = headB.next
        return None


headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(3)
headB.next = headA.next.next.next

test = Solution()
print(test.getIntersectionNode(headA,headB).val)