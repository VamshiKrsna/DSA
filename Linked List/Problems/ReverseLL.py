# Reversing a Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reversal(self,head):
        if not head:
            return None
        d = None
        h = head
        while(h):
            nn = h.next
            h.next = d
            d = h
            h = nn
        return d

    def traversal(self,head):
        if not head:
            return None
        temp = head
        while(temp):
            print(f"{temp.data}",end = "->")
            temp = temp.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.head.next.next = Node(30)
    ll.head.next.next.next = Node(40)
    rev = ll.reversal(ll.head)
    ll.traversal(rev)

