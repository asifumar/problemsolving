# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sum = l1.val + l2.val
        
        r = ListNode(sum%10)
        head = r

        if (sum>=10):
            carry = 1
        else :
            carry = 0

        l1 = l1.next
        l2 = l2.next

        #breakpoint()

        while l1 or l2 or carry == 1:

            if not (l1 or l2):
                r.next = ListNode(1)
                carry = 0


            elif not l1:
                r.next = ListNode( (l2.val + carry)%10)
                if (l2.val + carry)>=10:
                    carry = 1
                else:
                    carry = 0
                r = r.next
                l2 = l2.next

            elif not l2:
                r.next = ListNode( (l1.val + carry)%10)
                if (l1.val + carry)>=10:
                    carry = 1
                else:
                    carry = 0
                r = r.next
                l1 = l1.next

            else:
                r.next = ListNode( (l1.val + l2.val + carry)%10)
                
                if (l1.val + l2.val + carry)>=10:
                    carry = 1
                else:
                    carry = 0

                l1 = l1.next
                l2 = l2.next
                r = r.next

            #print(r.val)
            #breakpoint()
        
        while(head):
            print(head.val)
            head = head.next

        



l1 = ListNode(3)
l1.next = ListNode(7)
#l1.next.next = ListNode(5)
#l1.next.next.next = ListNode(4)

l2 = ListNode(9)
l2.next = ListNode(2)
#l2.next.next = ListNode(5)

test1 = Solution()
test1.addTwoNumbers(l1, l2)
