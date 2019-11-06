
print("PRINTING PATTERN $")
for i in range(4):
    for j in range(4):
        print("$ ",end="")
    print()

print()
print("PRINTING PATTERN #")
for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()

print()
print("PRINTING PATTERN &")
for i in range(4):
    for j in range(4-i ):
        print("& ",end="")
    print()


print("PRINTING PATTERN 9")
for i in range(5):
    for j in range(i+1):
        print("9 ",end="")
    print()
for i in range(4):
    for j in range(4-i):
        print("9 ",end="")
    print()





print("PRINTING PATTERN TRIANGLE")


def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
n = 5
triangle(n)


print("PRINTING PATTERN TRIANGLE")

n = 5
triangle(n)
def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")




n = 5
triangle(n)
def triangle(n):
    k = 2 * n + 2
    for i in range(n, 0):
        for j in range(0, k):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")







print("Printing Pattern of Triangle")


num=int(input("Enter the Number of rows "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()



print("Printing Pattern of Inverse Triangle")


num=int(input("Enter the Number of rows "))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()




print("Printing Pattern of Traiange & Inverse Triangle")


num=int(input("Enter the Number of rows "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()




