class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.left = self.right = None
    def enqueue(self,data):
        newnode = Node(data)
        if self.right:
            self.right.next = newnode
            self.right = self.right.next
            print(f"Enqueued {newnode.data}")
        else:
            self.right = self.left = newnode
            print(f"Enqueued {newnode.data}")
    def dequeue(self):
        if self.left:
            cur = self.left.data
            print(f"Dequeued {cur}")
            self.left = self.left.next
        else:
            print("Insufficient Nodes")
    def print(self):
        if self.left:
            cur = self.left
            while(cur):
                print(f"{cur.data}","->",end="")
                cur = cur.next
        else:
            print("Empty Queue")
if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.print()
