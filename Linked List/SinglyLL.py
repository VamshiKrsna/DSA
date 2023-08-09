# Implementation of Singly Linked List in Python :(Non Menu Driven)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def InsertAtBeginning(self,data):
        newnode = Node(data)
        if self.head is None:
             self.head = newnode
             print(f"Inserted {data} as head \n")
        else:
            temp = self.head
            self.head = newnode
            self.head.next = temp
            print(f"Inserted {data} as head \n")

    def InsertAtEnd(self,data):
        newnode = Node(data)
        newnode.next = None
        if self.head is None:
            self.head = newnode
            print("Successfully Inserted")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
            print("Inserted Node at end")


    def InsertByPosition(self,data,position):
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

    def DeletionAtBeginning(self):
        if self.head:
            dele = self.head.data
            self.head = self.head.next
            print(f"Deleted {dele}")
        else:
            print("No Head")

    def DeletionAtEnd(self):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
                dele = temp.data
                temp = None
            print(f"Deleted {dele}")
        else:
            print("No Head")

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
        if self.head:
            temp = self.head
            while temp:
                print(temp.data,end="->")
                temp = temp.next



if __name__ == '__main__':
    LL = SLL()
    LL.InsertAtBeginning(10)
    LL.InsertAtEnd(20)
    LL.InsertAtEnd(30)

    LL.display()












