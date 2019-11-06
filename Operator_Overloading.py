
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3= student (m1,m2)

        return s3

    def __gt__(self, other):
        R1=self.m1+self.m2
        R2=other.m1+other.m2
        if R1>R2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1,self.m2

    def __str__(self):
        return'{} {}'.format(self.m1,self.m2)

s1=student(55,66)
s2=student(77,88)

s3 = s1 + s2


if s1>s2:
    print ("s1 Wins")
else:
    print ("s2 Wins")

x = 9
print(x.__str__())

print(s1.__str__())

print(s1)
print(s2)
