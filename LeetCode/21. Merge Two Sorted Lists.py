# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
            arr1=list1
            arr2=list2
            l1=[]
            l2=[]
            while arr1!=None:
                
                l1.append(arr1.val)
                arr1=arr1.next

            
            while (arr2!=None):
                l2.append(arr2.val)
                arr2=arr2.next
            
            out=sorted(l1+l2)
            
            
            if len(out)==0:
                p=''
                
                return (ListNode(p))
           
            head = ListNode(out[0])
            e = 1
            tail = head

            while e < len(out):  
                tail.next = ListNode(out[e])
                tail = tail.next
                e+=1
            return head
          



