
Pos = -1
def search (list, n):
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()["pos"] = i
        return True
    return False

list = [5,8,7,6,9,3]
n = 9
if search (list,n):
    print ("Found at",pos+1)
else:
    print ("Not Found")

