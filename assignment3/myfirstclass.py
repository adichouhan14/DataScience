class Arithmatic:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

a=int(input("Enter First No : "))
b=int(input("Enter Second No : "))
print("1.   Addition")
print("2.   Substraction")
print("3.   Multiplication")
print("4.   Division")
choice=int(input("Enter Your Choice"))
arith=Arithmatic()
if choice==1:
    print(arith.add(a,b))
elif choice==2:
    print(arith.sub(a,b))
elif choice==3:
    print(arith.mul(a,b))
elif choice==4:
    print(arith.div(a,b))
else:
    print("Invalid Choice")


    