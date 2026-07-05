"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Copy={None:None}
        current = head 
        while current is not None:
            copy=Node(current.val)
            Copy[current]=copy
            current=current.next
        current=head
        while current:
            copy=Copy[current]
            copy.next=Copy[current.next]
            copy.random=Copy[current.random]
            current=current.next
        return Copy[head]