# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def removeNthFromEnd(self, head, n):
        # print("START")
        def lent(head):
            temp = head
            count = 0
            while head!=None:
                count += 1
                head = head.next
            # print(count)
            return count
        L = lent(head)
        if L==n:
            return head.next
        t = L-n
        count = 1
        temp = head
        while count!=t:
            temp = temp.next
            count += 1
        
        temp.next = temp.next.next
        
        return head
        