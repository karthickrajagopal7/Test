class A:
    def feature1(self):
        print('Feature 1 is working')
"""SINGLE LEVEL INHERITANCE"""
class B(A):
    def feature2(self):
        print('Feature 2 is working')
"""MULTI-LEVEL INHERITANCE"""
class C(B):
    def feature3(self):
        print('Feature 3 is working')
"""MULTIPLE LEVEL INHERITANCE"""
class D:
    def feature4(self):
        print('Feature 4 is working')
class E:
    def feature5(self):
        print('Feature 5 is working')
class F(D,E):
    def feature6(self):
        print('Feature 6 is working')
a1 = A()
b1 = B()
c1 = C()
f1 = F()

a1.feature1()
b1.feature1()
b1.feature2()
c1.feature1()
c1.feature2()
c1.feature3()
f1.feature4()
f1.feature5()
f1.feature6()