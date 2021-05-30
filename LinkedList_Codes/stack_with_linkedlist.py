class node :
    def __init__(self,data):
        self.data = data
        self.next = None

class stack :
    def __init__(self):
        self.head =None

    def push(self,data):
        
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode
        
    def pop(self):
        temp =self.head
        extra = temp.next
        print("pop element : " + str(self.head.data))
        del temp
        self.head = extra

    def peak(self):
        print("Stack's peak : "+str(self.head.data))

    def printlist(self):
        temp =self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = stack()
llist.head = node(10)

llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)

llist.pop()
llist.pop()

llist.peak()

llist.printlist()