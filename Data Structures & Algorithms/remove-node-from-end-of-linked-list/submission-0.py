# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        
        print("Our linked list contains:")
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

        dummy = ListNode(0)
        dummy.next=head
        current = head
        print("Adding dummy node before head- linked list contains:")
        print(dummy.val,end=" -> ")
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        slow=dummy
        fast=head
        # 2. fast move n steps first
        for _ in range(n):
            fast = fast.next
            
        # 3. if fast is not None, keep move the next 
        while fast:
            slow = slow.next
            fast = fast.next
            
        # 4. if fast.next is None: means that slow.next is the node which need to be removed  
        slow.next = slow.next.next
        
        return dummy.next

        return head
        