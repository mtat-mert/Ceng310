import random

#input_data = tuple(map(float,input().split()))
#input_val = input_data[0]
#input_index = int(input_data[1])
input_val = 31
input_index=31
random_list=[]
for i in range(random.randint(1,10)):
    random_list.append(random.randint(1,50))
len_list = len(random_list)

try:
    old_data = random_list[input_index]
    random_list[input_index] = input_val
    print("Index {0} is changed from {1} to {2}".format(input_index,old_data,input_val))

except:
    print("Don’t try buffer overflow attacks in Python!")


    
