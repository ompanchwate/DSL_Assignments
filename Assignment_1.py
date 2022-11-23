'''         Assignment no. 1
Name : Om Panchwate 
Roll no. 21468

In second year computer engineering class, group A students play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions)'''

# Remove Duplicate
def rem_duplicate(l1):
    l2 = []
    for i in range(0, len(l1)):
        flag = False
        for j in range(0, len(l2)):
            if l1[i] == l2[j]:
                flag = True
        if not flag:
            l2.append(l1[i])
    return l2


# Function to get intersection of SET
def intersection(l1, l2):
    l3 = []
    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            if l1[i] == l2[j]:
                l3.append(l1[i])
    return l3


# Function to get union of the both set
def union(l1, l2):
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
    for j in range(len(l2)):
        l3.append(l2[j])
    return rem_duplicate(l3)


# Function to find out the difference of the SET
def difference(u, inter):
    l3 = []
    # u = union(l1, l2)
    # inter = intersection(l1, l2)
    for i in range(len(u)):
        flag = False
        for j in range(len(inter)):
            if u[i] == inter[j]:
                flag = True
        if not flag:
            l3.append(u[i])

    return rem_duplicate(l3)

A = int(input("Enter the number of Student in Group A :  "))
se_Cricket = []
for i in range(1, A+1):
    a = input("Enter the name of Student {0} : ".format(i))
    se_Cricket.append(a)

B = int(input("Enter the number of Student in Group B :  "))
se_Badminton = []
for i in range(1, B+1):
    a = input("Enter the name of Student {0} : ".format(i))
    se_Badminton.append(a)


C = int(input("Enter the number of Student in Group C :  "))
se_Football = []
for i in range(1, C+1):
    a = input("Enter the name of Student {0} : ".format(i))
    se_Football.append(a)

print("List of students who play both cricket and badminton :", intersection(se_Cricket,se_Badminton))
u = union(se_Cricket,se_Badminton)
inter = intersection(se_Cricket,se_Badminton)
print("List of students who play either cricket or badminton but not both :",difference(u,inter))

inte_f_b = intersection(se_Football,se_Badminton)
inte_f_c = intersection(se_Football,se_Cricket)
print("Number of students who play neither cricket nor badminton",len(difference(union(inte_f_b,inte_f_c),se_Football)))
print("Number of students who play cricket and football but not badminton :",len(difference(union(se_Cricket, se_Football), se_Badminton)))