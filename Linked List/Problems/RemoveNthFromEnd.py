from SinglyLL import *

def remove_nth_from_end(sll,n):
    """
    Remove nth node from the end.
    Example :
    input:
        sll = 1->2->3->4->5 ; n = 2
    output:
         1->2->3->5
    """
    dummynode = Node(0)
    dummynode.next = sll.head
    l,r = dummynode,dummynode
    for i in range(n+1):
        l = l.next
    while l is not None:
        l = l.next
        r = r.next
    r.next = r.next.next
    return sll


if __name__ == '__main__':
    ll = SLL()
    ll.InsertAtBeginning(10)
    ll.InsertAtEnd(20)
    ll.InsertAtEnd(30)
    ll.InsertAtEnd(40)
    ll.InsertAtEnd(50)
    ll.display()
    print("\n")
    fin = remove_nth_from_end(ll,2) # LL after removing nth node.
    fin.display()