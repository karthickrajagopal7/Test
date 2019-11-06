class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def compare(self,other):
        if self.ram == other.ram:
            return True

c1 = computer('i5',16)
c2 = computer('i10',32)

print (c1.cpu,c1.ram)
print(c2.cpu,c2.ram)

if c1.compare(c2):
    print("SAMMMMMMMMMMMMMMMMMMMMMME")
else:
    print("DIFFERENT")
