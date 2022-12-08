class Search:
    def __init__(self, a, x):
        self.arr = a  # Stored the list into class data member self.arr
        self.n = len(self.arr)  # Stored length of the list
        self.x = x  # Stored the element which we want to search

    def sequentialSearch(self):
        for i in range(0, self.n):
            if self.arr[i] == self.x:
                print("Element found at index {0} ".format(i))
                return
        print("Element not found")

    def sentinelSearch(self):
        last = self.arr[self.n - 1]  # Stored the last Element of  the self.arr into last variable
        self.arr[self.n - 1] = self.x  # Stored the key at the last of the list

        i = 0
        while (self.arr[i] != self.x):
            i += 1

        # Again initialize the original element of the list at the last of the list in place of key
        self.arr[n - 1] = last

        # If i is 1 lesser than the length of the list or the last element is equal to the key THEN ELEMENT IS FOUND
        if ((i < self.n - 1) or (self.arr[self.n - 1] == self.x)):
            print(self.x, "is present at", i)
        else:
            print("Element not found")

    def binarysearch(self, start, end):
        if end >= start:
            mid = (start + (end-1)) // 2
            if self.arr[mid] == x:
                return mid
            elif self.arr[mid] > self.x:

                return obj.binarysearch(start, mid-1)
            else:
                return obj.binarysearch(mid+1, end)
        else:
            return -1


    def fibonacciSearch(self):
        pass

    def display(self):
        print(self.arr)



n = int(input("Enter the number of elements to be added : "))
a = []
for i in range(0, n):
    ele = int(input("Enter the element {0} : ".format(i)))
    a.append(ele)

x = int(input("Enter the element you want to Search : "))

obj = Search(a, x)
obj.display()

# MENU
exit = False
while not exit:
    print('''\n------Select the operation you want to perform :---------
        1) Linear Search
        2) Sentinel Search
        3) Binary Search
        4) Fibonacci Search
        5) Exit
    ''')

    option = int(input("Enter your choice : "))

    if option == 1:
        obj.sequentialSearch()
    elif option == 2:
        obj.sentinelSearch()
    elif option == 3:
        result = obj.binarysearch(0,n)
        if result != -1:
            print("Element is present at index ", result)
        else:
            print("Element is not present in array")
    elif option == 4:
        obj.fibonacciSearch()
    elif (option == 5):
        exit = True
    else:
        print("Invalid Choice")