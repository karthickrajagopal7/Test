class student:
    school = "St.Pauls"

    def __init__(self, m1, m2, m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m2(self):
        """accessor methods"""
        return self.m2
    def set_m1(self,value):
        self.m1 = value
        """mutator methods"""
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is a Student class......")
s1 = student(99,92,93)
s2 = student(49,89,93)

s2.set_m1(100)

print(s1.m1,s1.m2,s1.m3)
print(s2.m1,s2.m2,s2.m3)

print(s1.get_m2())

print(s1.avg())

print(student.getschool())
student.info()

