class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

ll1 = LL()
ll1.head = Node(10)
ll1.head.next = Node(20)
ll1.head.next = Node(30)
ll1.head.next = Node(40)

ll2 = LL()
ll2.head = Node(10)
ll2.head.next = Node(20)
ll2.head.next = Node(30)
ll2.head.next = Node(40)


head1 = ll1.head
head2 = ll2.head

def union(head1, head2):
    fin = []
    while head1.next:
        fin.append(head1.data)
    while head2.next and head2:
        fin.append(head2.data)
    fin = set(fin)
    fins = ""
    for i in fin:
        fins += i + " "
    return fins

print(union(head1, head2))