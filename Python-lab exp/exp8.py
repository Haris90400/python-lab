class A:
    def __init__(self,a): 
        self.var_a = a
    def disp(self):
        print(f"{self.var_a} I am class A")
    def mod(self,a):
        self.var_a=a 


class B(A):
    def __init__(self,a,b):
        A.__init__(self,a)
        self.var_b=b
    def disp(self):
        print(f"{self.var_b} I am class B")
    def mod(self,a,b):
        A.mod(self,a)
        self.var_b=b

class C(A):
    def __init__(self,a,c):
        A.__init__(self,a)
        self.var_c=c
    def disp(self):
        print(f"{self.var_c} I am class c")
    def mod(self,a,c):
        A.mod(self,a)
        self.var_c=c

class P(B,C):
    def __init__(self, a, b,c,p):
        B.__init__(self,a,b)
        C.__init__(self,a,c)
        self.var_p = p
    def disp(self):
        B.disp(self)
        C.disp(self)
        print(f"{self.var_p} I am class P")
    def mod(self,a,b,c,p):
        B.mod(self,a,b)
        C.mod(self,a,c)
        self.var_p=p

x=P("hi","hola","hello","bonjour")
x.disp()
x.mod("oy","oi","ei","yo")
x.disp()