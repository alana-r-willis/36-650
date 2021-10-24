def num_tri(n):
    if (not isinstance(n, int)):
        print("Invalid Input")
    elif (n < 0):
        print("Invalid Input") 
    else:
        x = 1
        for i in range(0, n):
            for j in range(0, i+1): 
             print(x, end=" ")
             x = x + 1
            print("\r")
 
n1 = 2.5
n2 = 3
n3 = 6
num_tri(n1)
num_tri(n2)
num_tri(n3)