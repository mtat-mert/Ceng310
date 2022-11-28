import fileinput
import re

student_list=[]
unlisted_students=[]
empty_groups=[]

for line in fileinput.input(files="studentList.txt"):
    line=line.strip('\n')
    student_list.append(str(line))
student_groups=[[str(s) for s in re.findall(r'\b\d+\b',line)] for line in fileinput.input(files="studentListGroup.txt")]




for student_group in student_groups:
    for student in student_group:
        if student not in student_list:
            print("Student ID:{0} is not registered so is taken out from the groups.".format(student))
            student_group.remove(student)
    if(len(student_group) < 5):
        empty_groups.append([student_groups.index(student_group),5-len(student_group)])

for student in student_list:
    student_found = False
    for student_group in student_groups:
        if student in student_group:
            student_found = True
            break;
    if(student_found == False):
        unlisted_students.append(student)
        print("Student ID:{0} is not in any student groups.".format(student))
        
try:
    for group_number,available_space in empty_groups:
        for i in range(available_space):
            print("Student ID:{0} is added to the empty space in the {1} group".format(unlisted_students[0],group_number+1))
            student_groups[group_number].append(unlisted_students[0])
            unlisted_students.pop(0)
except:
    print("Finished")
