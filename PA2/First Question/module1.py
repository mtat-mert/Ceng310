from turtle import color
import stacknque
import matplotlib.pyplot as plt
import time
import random


n=list(range(1,int(5e4),1000))
a=[]
b=[]

for i in n:
    a_list=[]
    for k in range(0,i):
        inte = random.randint(1,1000)
        a_list.append(inte)
    inte2=a
    empty_stack=stacknque.Stack()
    start=time.process_time_ns()
    for z in range(0,i):
        empty_stack.push(a_list.pop())
        if empty_stack.top() == 31:
            empty_stack.pop()
    while(not empty_stack.isempty()):
        a_list.append(empty_stack.pop())
    end=time.process_time_ns()
    a.append(end-start)
    start2=time.process_time_ns()
    inte2[:]=[value for value in inte2 if value!=31]
    end2=time.process_time_ns()
    b.append(end2-start2)
#plt.plot(n,a,color='r')
plt.plot(n,b,color='g')
plt.show()
