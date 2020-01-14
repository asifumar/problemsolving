class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {}
        newhead = Node(head.val)
        d[id(head)] = newhead
        tempnewhead = newhead
        temp = head

        while temp.next!= None:
            tempnewhead.next = Node(temp.next.val)
            d[id(temp.next)] = tempnewhead.next
            tempnewhead = tempnewhead.next
            temp = temp.next

        tempnewhead = newhead
        temp = head

        while temp!= None:
            if temp.random is None:
                tempnewhead.random = None
            else:
                tempnewhead.random = d[id(temp.random)]
            temp = temp.next
            tempnewhead = tempnewhead.next

        return newhead

headA = Node(7)
headA.next = Node(13)
headA.next.next = Node(11)
headA.next.next.next = Node(10)
headA.next.next.next.next = Node(1)

headA.random = headA.next
headA.next.random = headA
headA.next.next.random = headA.next.next.next.next
headA.next.next.next.random = headA.next.next
headA.next.next.next.next.random = headA

test = Solution()
t = test.copyRandomList(headA)
print(t.next.val)






        