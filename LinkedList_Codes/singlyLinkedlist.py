class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None


    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp =temp.next


    def push(self,new_no):
        new_head = node(new_no)
        new_head.next = self.head
        self.head = new_head


    def addAfter(self,new_num,past_num): 
        newnode = node(new_num)
        temp = self.head
        while (temp):
            if temp.data == past_num:
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next


    def insertend(self,new_data):
        newnode = node(new_data)
        end = self.head
        while(end.next):
            end = end.next
        end.next = newnode


    def addLast(self,newnum):
        newnode = node(newnum)
        temp =self.head
        while (temp):
            if temp.next == None:
                temp.next = newnode
                break
            temp = temp.next


    def length(self):
        count = 0
        temp= self.head
        while(temp):
            if temp.data != None:
                count = count+1
            temp = temp.next
        
        print("length of the linkedlist is : " + str(count))
        return (count)


    def search(self,number):
        temp = self.head
        while (temp):
            if (temp.data == number):
                print(str(number)+" is present in the linkedlist ")
                break
            elif (temp.next == None):
                print(str(number)+" is not present") 
            temp = temp.next


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

    def delete_list(self):
        temp = self.head 
        extra = None
        while(temp):
            extra = temp.next
            del temp.data
            temp = extra
        print("Your linked list is deteted")



    def getNth(self,index):
        count = 0
        temp = self.head
        while count<index :
            count=count+1
            if count == index :
                print(str(index)+ "th index is : " +str(temp.data))
            temp = temp.next

    def middlelment(self):
        temp1 = self.head
        temp2 = self.head
        while (temp2) and (temp1) :
            if temp2.next == None :
                print(str(temp1.data) + " is the middle element in linkedlist ")
                break
            elif temp2.next.next == None:
                print(str(temp1.data) + " is the middle element in linkedlist ")
                break
            else:
                temp1=temp1.next
                temp2=temp2.next.next

    
    def reverse_list(self):
        temp = self.head
        current = None
        while (temp):
            next = temp.next
            temp.next = current
            current = temp
            temp = next
        self.head = current

    def nth_from_end(self,nth):
        temp = self.head
        llist_length = (llist.length())
        NTH_TERM = (llist_length)-nth 
        if nth > llist_length:
            print("Given number is more then total node in linkedlist.")      
        
        while temp:
            if NTH_TERM == 0:
                print("Nth node from the end is :"+str(temp.data))
            temp = temp.next
            NTH_TERM = NTH_TERM-1

    def count_num(self,search):
        temp = self.head
        count = 0
        while (temp):
            if temp.data == search:
                count = count+1
            temp = temp.next
        print("Search number is present " + str(count)+ " times in linked list. ")

    def detect_loop(self):
        temp = self.head
        current = self.head
        while (current and temp and current.next):
            temp = temp.next
            current = current.next.next
            if current.data == temp.data:
                print("loop found")
                break
        if current == None or temp == None or current.next == None:
            print("loop not found")


llist = linkedlist()

llist.head = node(10)
first = node(11)
second = node(12)
third = node(13)
fourth = node(14)
fifth = node(15)
sixith = node(16)


llist.head.next = first
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixith
#sixith.next = third
#llist.push(22)

#llist.addAfter(44,2)

#llist.addLast(123)
#llist.addLast(129)
#llist.addLast(100)
#llist.addLast(150)
#llist.insertend(100)

#llist.length()

#llist.search(44)

llist.delete(16)
llist.delete(15)
#llist.getNth(8)

#llist.middlelment()

#llist.reverse_list()

#llist.nth_from_end(5)

#llist.count_num(11)

#llist.delete_list()

llist.detect_loop()

llist.printlist()