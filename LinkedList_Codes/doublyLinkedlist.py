class node :
    def __init__(self,data):
        self.data =data
        self.next = None
        self.previous  = None

class linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def Add_at_start(self,new_data):
        newNode = node(new_data)
        self.head.previous = newNode
        newNode.next = self.head
        self.head =newNode


    def addAfter(self,new_data,past_num):
        
        temp = self.head
        while (temp):
            if temp.data == past_num:
                newnode = node(new_data)
                newnode.previous = temp
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next

    def addLast(self,new_data):
        temp = self.head
        while(temp):
            if temp.next == None:
                newnode = node(new_data)
                newnode.previous = temp
                temp.next = newnode
                break
            temp = temp.next
        
    def delete(self,number):
        temp = self.head 
        while (temp):
            if temp.data == number and temp.previous == None:
                self.head = temp.next
                temp.next.previous = None
                break

            elif temp.data==number and temp.next ==None:
                temp.previous.next = None
                break

            elif temp.data == number :
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                
        
            temp = temp.next

    def print_reverse_llist(self):
        temp = self.head
        while(temp):
            if temp.next == None:
                reverse_temp = temp
                while (reverse_temp):
                    print(reverse_temp.data)
                    reverse_temp=reverse_temp.previous
            temp = temp.next

    def reverse_list(self):
        temp = None
        current = self.head

        while(current):
            temp = current.previous
            current.previous = current.next
            current.next = temp
            current = current.previous

        if temp!=None:
            self.head = temp.previous

    


llist = linkedlist()
llist.head = node(10)
first = node(11)
second = node(12)
third = node(13)
fourth = node(14)

llist.head.next = first
first.previous = llist.head
first.next = second
second.previous = first
second.next = third
third.previous = second
third.next = fourth
fourth.previous =third

#llist.Add_at_start(9)
#llist.Add_at_start(8)
  
#llist.addAfter(11.5,11)

#llist.addLast(15)
#llist.delete(10)
#llist.delete(11)
#llist.print_reverse_llist()
#llist.reverse_list()
llist.printlist()