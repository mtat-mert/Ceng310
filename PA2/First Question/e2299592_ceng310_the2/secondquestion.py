import stacknque

#second question solution
def prime_finder(first_queue,n):
    selected=first_queue.dequeue()
    first_queue.enqueue(selected) # puts element to last
    while selected < n**(1/2):
        if selected != first_queue.front():
            if first_queue.front()%selected != 0:
                first_queue.enqueue(first_queue.dequeue())
            elif first_queue.front()%selected == 0:
                first_queue.dequeue()
        else:
            temp=first_queue.dequeue()
            first_queue.enqueue(temp) # if comes to itself sends itself to last
            selected=first_queue.dequeue()
            first_queue.enqueue(selected)
    return first_queue