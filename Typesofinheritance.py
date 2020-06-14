# single Inheritance
class P:
    @staticmethod
    def m1():
        print("Parent method")


class C(P):
    @staticmethod
    def m2():
        print("Child Method")


# c = C()
# c.m1()
# c.m2()


# Multi level Inheritance
class CC(C):
    @staticmethod
    def m3():
        print("Sub child method")


c = CC()
c.m1()
c.m2()
c.m3()


# hierarchical Method
class CCP(P):
    @staticmethod
    def m4():
        print("Sub child method of class CCP")


c = CCP()
c.m4()


# Multiple Inheritance

class P1:
    @staticmethod
    def m1():
        print("Parent 1 method")


class P2:
    @staticmethod
    def m2():
        print("Parent 2 method")


class CMI(P1, P2):
    @staticmethod
    def m3():
        print("Child method")


c = CMI()
c.m1()
c.m2()
c.m3()
