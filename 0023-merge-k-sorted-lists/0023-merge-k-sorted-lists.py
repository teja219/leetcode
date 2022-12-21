# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        counter = [0 for x in range(len(lists))]
        
        lis = []
        
        for i in range(len(lists)):
            if lists[i] is not None:
                lis.append((lists[i].val,lists[i].next))
        
        heapq.heapify(lis)
        head = None
        tail = None
        while len(lis)!=0:
            (ans,nxt) = heapq.heappop(lis)
            if nxt!=None:
                heapq.heappush(lis,(nxt.val,nxt.next))
            if head == None:
                head = ListNode(ans,None)
                tail = head
            else:
                tail.next = ListNode(ans,None)
                tail = tail.next
                
        return head
                
        