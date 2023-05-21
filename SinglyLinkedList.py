class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def insertInBetween(self, data, position):
        if position < 0:
            print("Invalid position.")
            return
        newNode = Node(data)
        if position == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            count = 0
            current = self.head
            while count < position - 1 and current:
                current = current.next
                count += 1
            if current is None:
                print("Invalid position.")
                return
            newNode.next = current.next
            current.next = newNode

    def deleteAtBeg(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def deleteByPos(self, position):
        if position < 0:
            print("Invalid position.")
            return
        if self.head is None:
            print("List is empty.")
            return
        if position == 0:
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while count < position - 1 and current:
            current = current.next
            count += 1
        if current is None or current.next is None:
            print("Invalid position.")
            return
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()


ll.insertAtBeg(30)
ll.insertAtBeg(20)
ll.insertAtBeg(10)
ll.insertAtEnd(40)
ll.insertAtEnd(50)
ll.insertInBetween(25, 2)

ll.display()

ll.deleteAtBeg()
ll.deleteAtEnd()
ll.deleteByPos(2)

ll.display()
