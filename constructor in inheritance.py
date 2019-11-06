
class A:
    def __init__(self):
        print('INIT AAAAAAA')
    def feature1(self):
        print('Feature 1 is working')

class B():
    def __init__(self):
        print('INIT BBBBBBB')
    def feature2(self):
        print('Feature 2 is working')

class C(B,A):
    def __init__(self):
        super().__init__()
        print('INIT CCCCCC')
    def feature3(self):
        print('Feature 3 is working')

a1 = A()
print('\n')
b1 = B()
print('\n')
c1 = C()
print('\n')


print('\n')
a1.feature1()
c1.feature1()












class A:
    def __init__(self):
        print('INIT AAAAAAA')
    def feature1(self):
        print('Feature 1 AA is working')

class B():
    def __init__(self):
        print('INIT BBBBBBB')
    def feature1(self):
        print('Feature 1 BB is working')

class C(B,A):
    def __init__(self):
        super().__init__()
        print('INIT CCCCCC')
    def feature3(self):
        print('Feature 3 is working')

a1 = A()
print('\n')
b1 = B()
print('\n')
c1 = C()
print('\n')

c1.feature1()


