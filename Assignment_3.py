'''         Assignment no. 3
Name : Om Panchwate 
Roll no. 21468

Write a Python program to compute following computation on matrix:
a) Addition of two matrices 
B) Subtraction of two matrices
c) Multiplication of two matrices 
d) Transpose of a matrix'''

class MatrixOp:
    # Print Matrix
    def printMatrix(self,m1,m2):
        print("MAT 1 = ",end=" ")
        for i in range(0,len(m1)):
            print(m1[i],end="\n\t ")
        print()
        
        print("MAT 2 = ",end=" ")
        for i in range(0,len(m2)):
            print(m2[i],end="\n\t ")

        print()
        
    # Add matrix
    def addMatrix(self,m1,m2):
        if(len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
            self.printMatrix(m1,m2)
            result = []
            for i in range(0,len(m1)):    
                a = []
                for j in range(0,len(m1[i])): 
                    a.append(m1[i][j] + m2[i][j])
                result.append(a)

            print("Addition = ")
            for i in range(0,len(result)):
                print(result[i])
        else:
            print("Addition not possible")

    # Subtract Matrix
    def subMatrix(self,m1,m2):
        if(len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
            self.printMatrix(m1,m2)
            result = []
            for i in range(0,len(m1)):    
                a = []
                for j in range(0,len(m1[i])): 
                    a.append(m1[i][j] - m2[i][j])
                result.append(a)

            print("Subtraction = ")
            for i in range(0,len(result)):
                print(result[i])
        else:
            print("Subtraction not possible")

    # Multiply Matrix
    def mulMatrix(self,m1,m2):
        self.printMatrix(m1,m2)
        result = []
        
        for row in range(len(m1)):
            curr_row = []
            for col in range(len(m2[0])):
                curr_row.append(0)
            result.append(curr_row)

        for i in range(0,len(m1)):
            for j in range(0,len(m2[0])):
                mul = 0
                for k in range(0,len(m2)):
                    mul += m1[i][k] * m2[k][j]
                result[i][j] = mul
        
        print("Multiplication = ")
        for i in range(0,len(result)):
            print(result[i])

    # Transpose Matrix
    def transpose(self,m1,m2):
        self.printMatrix(m1,m2)

        # Transpose mat-I
        m1_trans = []
        for row in range(len(m1[0])):
            curr_row = []
            for col in range(len(m1)):
                curr_row.append(0)
            m1_trans.append(curr_row)
        
        # iterate through rows
        for i in range(len(m1)):
            a = []
            # iterate through columns
            for j in range(len(m1[0])):
                m1_trans[j][i] = m1[i][j]
                
        print("Transpose of Mat-I = ")
        for i in range(0,len(m1_trans)):
            print(m1_trans[i])

        # Transpose mat-II
        m2_trans = []
        for row in range(len(m2[0])):
            curr_row = []
            for col in range(len(m2)):
                curr_row.append(0)
            m2_trans.append(curr_row)
        
        # iterate through rows
        for i in range(len(m2)):
            a = []
            # iterate through columns
            for j in range(len(m2[0])):
                m2_trans[j][i] = m2[i][j]
                
        print("Transpose of Mat-I = ")
        for i in range(0,len(m2_trans)):
            print(m2_trans[i])
# Class MatrixOp End


# Read Matrix-I
print("Matrix - I :")
m1r  = int(input("Enter the number of rows in M-I : "))
m1c = int(input("Enter the number of Column in M-II : "))
m1 = []
for i in range(1,m1r+1):
    a = []
    for j in range(1,m1c+1):
        a.append(int(input("Enter the value of m[{0}][{1}] : ".format(i,j))))
    m1.append(a)

# Read Matrix-II
print("Matrix - II :")
m2r = int(input("Enter the number of rows in M-II : "))
m2c = int(input("Enter the number of Column in M-II : "))
m2 = []
for i in range(1,m2r+1):
    a = []
    for j in range(1,m2c+1):
        a.append(int(input("Enter the value of m[{0}][{1}] : ".format(i,j))))
    m2.append(a)


# Menu
obj = MatrixOp()
exit = False

while not exit:
    print('''\n------Select the operation you want to perform :---------
        1) Addition of two matrices 
        2) Subtraction of two matrices
        3) Multiplication of two matrices 
        4) Transpose of a matrix
        5) Exit
    ''')

    option = int(input("Enter your choice : "))

    if(option == 1):
        obj.addMatrix(m1,m2)

    elif option == 2:
        obj.subMatrix(m1,m2)

    elif option == 3 :
        if(m1c == m2r):
            obj.mulMatrix(m1,m2)
        else:
            print("Multiplication is not possible")
    
    elif option == 4:
        obj.transpose(m1,m2)
        
    elif option == 5:
        exit = True

    else:
        print("Wrong Option!")