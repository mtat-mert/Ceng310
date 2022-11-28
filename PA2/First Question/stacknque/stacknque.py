
class Stack:

    def __init__(self):
       self._data=[]
    def isempty(self):
        return len(self._data)==0
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.isempty():
            raise Empty("Stack is Empty")
        return self._data[-1]
    def pop(self):
        if self.isempty():
            raise Empty("Stack is Empty")
        return self._data.pop()

class Queue:
    def __init__(self):
       self._data=[]
    def enqueue(self,e):
        self._data.append(e)
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data.pop(0)
    def front(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[0]
    def isempty(self):
        return len(self._data)==0





class Empty(Exception):
     def __init__(self,message="Empty Variable"):
        self.message = message
        super().__init__(self.message)
     pass
