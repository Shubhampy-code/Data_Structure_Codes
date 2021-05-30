class Stack():
    def __init__(self):
        self.max = 100
        self.array = [None]*self.max
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True

        else:
            return False

    def isFull(self):
        if self.top == self.max-1:
            return True

        else:
            return False
    
    def push(self,data):
        if self.isFull():
            print("stack is full")
        else:
            self.top = self.top+1
            self.array[self.top] = data
            print(str(data) + " is insertted successfully at location: " + str(self.top))

    def pop(self):
        if self.isEmpty():
            print("stack is empty")

        else:
            print("pop element : "+ str(self.array[self.top]))
            self.array[self.top] = None
            self.top = self.top-1

s=Stack()
if (s.isEmpty()):
    print ("Empty")
s.pop()
s.push(10)
s.push(11)
s.push(12)
s.push(13)

s.pop()

    
