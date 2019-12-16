# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head.next:
            return head
        if not head.next.next:
            self.t = head.next
            self.t.next = head
            head.next = None
            return self.t

        self.p = head
        head = head.next
        self.n = head.next
        self.p.next = None
        
        while head:
            head.next = self.p
            self.p = head
            head = self.n
            if self.n.next:
                self.n = self.n.next
            else:
                head.next = self.p
                break

        return head

def pr(head):
    while(head):
        print(head.val)
        head = head.next

one = ListNode(1)
one.next = ListNode(2)
#one.next.next = ListNode(4)

test = Solution()
result = test.reverseList(one)
pr(result)