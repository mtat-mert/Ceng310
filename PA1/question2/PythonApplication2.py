import random


#if the index given is higher than 5 (length of the list) it prints dont try buffer overflow attacks in python

input_data = tuple(map(float,input().split()))
input_index = int(input_data[0])
input_val = input_data[1]

random_list=[]
for i in range(5):
    random_list.append(random.randint(1,50))
len_list = len(random_list)

try:
    old_data = random_list[input_index]
    random_list[input_index] = input_val
    print("Index {0} is changed from {1} to {2}".format(input_index,old_data,input_val))


except:
    print("Don\'t try buffer overflow attacks in Python!")


    