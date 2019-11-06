class student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def sum(self, a=None, b=None, c=None):
        s=0
        if a != None and b != None and c != None:
            s=a+b+c
        elif a != None and b != None:
            s=a+b
        else:
            s=a
        return s

s1=student(55,66,77)

print(s1.sum(66,11,22))

