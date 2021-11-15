print("this is my print statement")

var2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, num in enumerate(var2):
    var3 = num + var2[i-1]
    print(var3)