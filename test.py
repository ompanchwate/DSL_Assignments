'''Write a Python program to compute following computation on matrix:
a) Addition of two matrices 
B) Subtraction of two matrices
c) Multiplication of two matrices 
d) Transpose of a matrix'''

class MatrixOp:

    def __init__(self):
        # Read Matrix-I
        print("Matrix - I :")
        m1r  = int(input("Enter the number of rows in M-I : "))
        m1c = int(input("Enter the number of Column in M-II : "))
        self.m1 = []
        for i in range(1,m1r+1):
            a = []
            for j in range(1,m1c+1):
                a.append(int(input("Enter the value of m[{0}][{1}] : ".format(i,j))))
            self.m1.append(a)

        # Read Matrix-II
        print("Matrix - II :")
        m2r = int(input("Enter the number of rows in M-II : "))
        m2c = int(input("Enter the number of Column in M-II : "))
        self.m2 = []
        for i in range(1,m2r+1):
            a = []
            for j in range(1,m2c+1):
                a.append(int(input("Enter the value of m[{0}][{1}] : ".format(i,j))))
            self.m2.append(a)

        

    # Print Matrix
    def printMatrix(self):
        print("MAT 1 = ",end=" ")
        for i in range(0,len(self.m1)):
            print(self.m1[i],end="\n\t ")
        print()
        
        print("MAT 2 = ",end=" ")
        for i in range(0,len(self.m2)):
            print(self.m2[i],end="\n\t ")

        print()
        
    # Add matrix
    def addMatrix(self):
        self.printMatrix()
        result = []
        for i in range(0,len(self.m1)):    
            a = []
            for j in range(0,len(self.m1[i])): 
                a.append(self.m1[i][j] + self.m2[i][j])
            result.append(a)

        print("Addition = ")
        for i in range(0,len(result)):
            print(result[i])

    # Subtract Matrix
    def subMatrix(self):

        self.printMatrix()
        result = []
        for i in range(0,len(self.m1)):    
            a = []
            for j in range(0,len(self.m1[i])): 
                a.append(self.m1[i][j] - self.m2[i][j])
            result.append(a)

        print("Subtraction = ")
        for i in range(0,len(result)):
            print(result[i])

    # Multiply Matrix
    def mulMatrix(self):
        self.printMatrix()
        if(len(self.m1[0]) == len(self.m2)):
            result = []
            
            for row in range(len(self.m1)):
                curr_row = []
                for col in range(len(self.m2[0])):
                    curr_row.append(0)
                result.append(curr_row)

            for i in range(0,len(self.m1)):
                for j in range(0,len(self.m2[0])):
                    mul = 0
                    for k in range(0,len(self.m2)):
                        mul += self.m1[i][k] * self.m2[k][j]
                    result[i][j] = mul
            
            print("Multiplication = ")
            for i in range(0,len(result)):
                print(result[i])
        else:
            print("Multiplication is not Possible.")

        # Transpose Matrix
    def transpose(self):
        self.printMatrix()

        # Transpose mat-I
        m1_trans = []
        for row in range(len(self.m1[0])):
            curr_row = []
            for col in range(len(self.m1)):
                curr_row.append(0)
            m1_trans.append(curr_row)
            
        # iterate through rows
        for i in range(len(self.m1)):
            a = []
            # iterate through columns
            for j in range(len(self.m1[0])):
                m1_trans[j][i] = self.m1[i][j]
                    
        print("Transpose of Mat-I = ")
        for i in range(0,len(m1_trans)):
            print(m1_trans[i])
        

        # Transpose mat-II
        m2_trans = []
        for row in range(len(self.m2[0])):
            curr_row = []
            for col in range(len(self.m2)):
                curr_row.append(0)
            m2_trans.append(curr_row)
        
        # iterate through rows
        for i in range(len(self.m2)):
            a = []
            # iterate through columns
            for j in range(len(self.m2[0])):
                m2_trans[j][i] = self.m2[i][j]
                
        print("Transpose of Mat-I = ")
        for i in range(0,len(m2_trans)):
            print(m2_trans[i])
# Class MatrixOp End




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
        obj.addMatrix()

    elif option == 2:
        obj.subMatrix()

    elif option == 3 :
        obj.mulMatrix()
    
    elif option == 4:
        obj.transpose()
        
    elif option == 5:
        exit = True

    else:
        print("Wrong Option!")