'''         Assignment no. 2
Name : Om Panchwate 
Roll no. 21468

Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string'''
class StringOperation:
    def longest(self,string):
        string = string.split()
        length = []
        for i in range(0,len(string)):
            count = 0
            for i in range(0,len(string[i])):
                count += 1
            length.append(count)

        longest = length[0]
        for i in range(1,len(length)):
            if longest < length[i]:
                longest = length[i]

        for i in range(len(length)):
            if longest == length[i]:
                return string[i]

    def occurence(self,char,string):
        count = 0
        for i in range(0,len(string)):
            if string[i] == char:
                count+=1
        return count
        
    def palindrome(self,string):
        rev = string[::-1]
        if (string == rev):
            print("String is a Palindrome")
        else:
            print("String is not a Palindrome")

    def substring(self,string,sub):
        string = string.split()
        for i in range(0,len(string)):
            if(string[i] == sub):
                return i

    def wordoccur(self,string):
        print('''The occurrences of each word in "{0}" : '''.format(string))
        string = string.split() 
        repeat = []
        for i in range(0,len(string)):
            count = 1
            if string[i] not in repeat:
                for j in range(i+1,len(string)):
                    if string[i] == string[j]:
                        repeat.append(string[i])
                        count+=1
                
                print(string[i],"=",count)

string = input("Enter the string : ")

s1 = StringOperation()
#Menu

exit = False

while not exit:
    print('''\n------Select the operation you want to perform :---------
        1) To display word with the longest length
        2) To determines the frequency of occurrence of particular character in the string
        3) To check whether given string is palindrome or not
        4) To display index of first appearance of the substring
        5) To count the occurrences of each word in a given string
        6) Exit
    ''')

    option = int(input("Enter your choice : "))

    if(option == 1):
        print("word with the longest length is :",s1.longest(string))

    elif option == 2:
        char = input("Enter the character you want to count : ")
        print("frequency of occurrence of {0} character in the string :".format(char),s1.occurence(char,string))

    elif option == 3 :
        
        # print("check whether given string is palindrome or not :",palindrome(string))
        s1.palindrome(string)
    
    elif option == 4:
        sub = input("Enter the substring you want to find out : ")
        print("index of first appearance of the {0} :".format(sub),s1.substring(string,sub))

    elif option == 5:
        s1.wordoccur(string)
    
    elif option == 6:
        exit = True
    
    else:
        print("Wrong Option!")