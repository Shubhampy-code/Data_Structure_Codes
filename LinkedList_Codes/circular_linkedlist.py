class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        if self.head != None:                
            while(temp):
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break

    def push(self,number):
        new_node = node(number)
        temp = self.head
        new_node.next = self.head
        
        if self.head != None:
            while temp.next!= self.head:
                temp = temp.next
            temp.next = new_node

        else:
            new_node.next = new_node

        self.head = new_node

    def delete(self,number):
        temp = self.head
        while (temp):
            if self.head.data == number:
                self.head = temp.next
                break

            
            elif temp.next.data == number:
                temp.next = temp.next.next   
                break 
            temp = temp.next

            

cllist = circular_linkedlist()
#cllist.head = node(10)

cllist.push(9)
cllist.push(8)
cllist.push(7)
cllist.push(6)

cllist.delete(6)

cllist.printlist()
