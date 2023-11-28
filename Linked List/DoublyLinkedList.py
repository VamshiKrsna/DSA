# Implementation of Doubly Linked List in Python :(Non Menu Driven)
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def InsertAtBeginning(self,data):
        self.len += 1
        nn = Node(data)
        if not self.head:
            self.head = nn
            self.tail = nn
        else:
            nn.next = self.head
            self.head.prev = nn
            self.head = nn


    def InsertAtEnd(self, data):
        self.len += 1
        nn = Node(data)
        if not self.head:
            self.head = nn
            self.tail = nn
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = nn
            nn.prev = temp
            self.tail = nn

    def DeleteAtBeginning(self):
        if not self.head:
            print("No Head, Can't Delete at beginning \n")
        else:
            self.head = self.head.next
            self.len -= 1
            self.head.prev = None
            print("Deleted at beginning \n")

    def DeleteAtEnd(self):
        if not self.head:
            print("No Head, Can't Delete at end \n")
        else:
            self.len -= 1
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            self.tail = temp.prev
            print(f"Deleted {temp.data} at end \n")

    def DeleteNode(self,data):
        if not self.head:
            print(f"Cant Delete {data} \n")
        else:
            self.len -= 1
            temp = self.head
            while temp.data != data:
                temp = temp.next
            if not temp.prev:
                self.head = temp.next
                self.head.prev = None
            elif not temp.next:
                temp.prev.next = None
                self.tail = temp.prev
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            print(f"Deleted {data} \n")

    def TraverseForward(self):
        if not self.head:
            print("DLL IS EMPTY, CAN'T TRAVERSE \n")
        else:
            temp = self.head
            while temp:
                print(temp.data,end = "->")
                temp = temp.next
            print("\n")
    def TraverseBackward(self):
        if not self.head:
            print("DLL IS EMPTY, CAN'T TRAVERSE \n")
        else:
            temp = self.tail
            while temp:
                print(temp.data, end="<-")
                temp = temp.prev
            print("\n")

    def GetLength(self):
        return self.len


if __name__ == '__main__':
    LL = DLL()
    LL.InsertAtBeginning(10)
    LL.InsertAtEnd(20)
    LL.InsertAtEnd(30)
    LL.TraverseForward()
    LL.TraverseBackward()
    LL.DeleteNode(20)
    LL.TraverseForward()
