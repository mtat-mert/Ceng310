import stacknque
from firstquestion import transfer
from secondquestion import prime_finder
from thirdquestion import normal_sort

#first question driver
first_list=list(range(1,10))
first_stack=stacknque.Stack()
second_stack=stacknque.Stack()
for i in first_list:
    first_stack.push(i)
print("First Stack")
first_stack._print()
print("Second Stack")
second_stack._print()
print("Transfer Function")
transfer(first_stack,second_stack)
print("First Stack")
first_stack._print()
print("Second Stack")
second_stack._print()

#second question driver
n=200
second_list=list(range(2,n+1))

#creation of queue's for second question
first_queue=stacknque.Queue()
result_queue=stacknque.Queue()

print("Queue of numbers")
for i in second_list:
    first_queue.enqueue(i)
print(second_list)
print("Primes within the queue")
result=prime_finder(first_queue,n)
result._print()


#third question driver
list_q3=[0, 2, -3, -5, -5, -5, 6, -7, 8, -9, 10, -20]
que_q3=stacknque.Queue()
for i in list_q3:
    que_q3.enqueue(i)
sorted_que=normal_sort(que_q3)
print("Absolute Sorted Queue")
print(list_q3)
print("Normal Sorted Queue")
sorted_que._print()