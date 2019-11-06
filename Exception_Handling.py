
a = 9
b = 0

try:
    print ("Resource Open")
    print(a/b)
    k=int(input("Enter the number : "))
    print(k)

except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by zero...", e)
except ValueError as e:
    print ("Invalid Input")
except Exception as e:
    print ("Something went wrong...", e)

finally:
    print ("Resource Closed")

