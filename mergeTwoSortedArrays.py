# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.curr = ListNode(0)
        self.head = self.curr
        
        while l1 and l2:
            if (l1.val<l2.val):
                self.curr.next = l1
                self.curr = self.curr.next
                l1 = l1.next
            else:
                self.curr.next = l2
                self.curr = self.curr.next
                l2 = l2.next
        self.curr.next = l1 or l2
        return self.head.next
    
def pr(head):
    while(head):
        print(head.val)
        head = head.next
    

one = ListNode(1)
one.next = ListNode(2)
one.next.next = ListNode(4)

two = ListNode(1)
two.next = ListNode(3)
two.next.next = ListNode(5)

test = Solution()
result = test.mergeTwoLists(one, two)
pr(result)
