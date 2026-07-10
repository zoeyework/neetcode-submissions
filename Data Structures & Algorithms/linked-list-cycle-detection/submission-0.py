# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()  # 使用 set 儲存節點，查詢速度為 O(1)
        current = head
        
        while current:
            if current in seen:  # 如果節點已經存在，表示有環
                return True
            seen.add(current)
            current = current.next
            
        return False