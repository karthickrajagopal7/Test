class computer:
    def __init__(self):
        self.name = 'Karthi'
        self.age = 28

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()

c1.name='Jaya'
c1.age=27

if c1.compare(c2):
    print('They are same')
else:
    print('They are different')

print(c1.name,c1.age)
print(c2.name,c2.age)