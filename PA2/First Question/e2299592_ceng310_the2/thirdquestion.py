import stacknque

def normal_sort(var_que):
    help_stack=stacknque.Stack()
    len_found = False
    len_que=0
    while not var_que.isempty() and len_found == False:
        len_que+=1
        help_stack.push(var_que.dequeue())
        if var_que.isempty():
            len_found == True
    while not help_stack.isempty():
        var_que.enqueue(help_stack.pop())
    while not var_que.isempty():
        max_val=var_que.dequeue()
        if not var_que.isempty():
            for i in range(0,len_que):
                if max_val <= var_que.front():
                    temp=max_val
                    max_val=var_que.dequeue()
                    var_que.enqueue(temp)
        help_stack.push(max_val)
    while not help_stack.isempty():
        var_que.enqueue(help_stack.pop())
    return var_que