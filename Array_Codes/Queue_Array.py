class Queue():

    def __init__(self):
        self.max = 5
        self.array = [None]*self.max
        self.rear = -1
        self.front = -1

    def isEmpty(self):
        if self.front == -1 or self.front < self.rear:
            return True
        else:
            return False

    def isfull(self):
        if self.front == self.max-1 :
            return True
        
        else:
            return False

    def Enqueue(self,data):
        if self.isfull():
            print("Queue is full")
        
        else:
            self.front = self.front+1
            self.array[self.front] = data
            if self.rear == -1:
                self.rear = self.rear+1 
            print(str(data) + " is insertted successfully at location: " + str(self.front))

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is already empty" )
        else:
            print(str(self.array[self.rear]) + " is Dequeue successfully at location: " + str(self.rear) )
            self.array[self.rear]= None
            self.rear = self.rear+1


q=Queue()
q.Dequeue()
q.Enqueue(10)
q.Enqueue(11)
q.Enqueue(12)
q.Enqueue(13)
#q.Enqueue(14)


q.Dequeue()
q.Dequeue()
q.Dequeue()
q.Dequeue()
q.Enqueue(14)
q.Dequeue()
q.Dequeue()