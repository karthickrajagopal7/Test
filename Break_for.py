av = 5
x=int(input("How many Candies do you want ? "))
for i in range(x):
    if i>=av:
        print('OUT OF STOCK')
        break
    print('CANDY')
print('Thanks')
