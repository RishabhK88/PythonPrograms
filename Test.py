print("Hello World")
print("*"*10)
i = 1

f = open("Rishabh.txt", "w")
f.write("Hey")
f.close()
f = open("Rishabh.txt", "a")
f.write("Rishabh")
f.close()


# Code with Harry Exercise
n = int(input("Enter the number of rows: "))
x = bool(int((input("Enter(0/1): "))))
if x is True:
    i = 1
    while(i <= n):
        print("*"*i)
        i += 1
elif x is False:
    j = 1
    while(j <= n):
        print(" "*(n-j), "*"*j)
        j += 1
