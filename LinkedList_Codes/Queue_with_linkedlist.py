class node:
    def __init__(self,data):
        self.data=data
        self.next = None

class queue:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp =temp.next

    def enqueue(self,new_num):
        new_node = node(new_num)
        new_node.next = self.head
        self.head=new_node

    def dequeue(self):
        temp =self.head
        while(temp):
            if temp.next.next == None:
                print("Dequeue element : " + str(temp.next.data))
                temp.next = None
                temp.next
              #  break
            temp = temp.next

llist = queue() 

llist.head = node(10)

llist.enqueue(9)
llist.enqueue(8)
llist.enqueue(7)
llist.enqueue(6)
llist.enqueue(5)
llist.enqueue(4)

llist.dequeue()
llist.dequeue()

llist.printlist()