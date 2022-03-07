import cmath
import math
import sys
def get_float(msg,allow_zero):
    x=None
    while x is None:
        try:
            x=float(input(msg))
            if not allow_zero and abs(x)<sys.float_info.epsilon:
                print("zero is not allow")
                x=None
        except ValueError as err:
            print(err)
    return x

print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a=get_float("enter a: ",False)
b=get_float("enter b: ",True)
c=get_float("enter c: ",True)

x1=None
x2=None
dis=(b**2)-(4*a*c)
if dis==0:
    x1=-(b/(2*a))
else:
    if dis>0:
        root=math.sqrt(dis)
    else:
        root=cmath.sqrt(dis)
    x1=(-b+root)/(2*a)
    x2=(-b-root)/(2*a)

def change(x):
    if x==0:return str("")
    else:return str(str(x)+"x")
equation=("{0}x\N{SUPERSCRIPT TWO}{1}{2}=0 \n"
          "\N{RIGHTWARDS ARROW}x={3} ".format(a,change(b),change(c),x1))
if x2 is not None:
    equation+="or x={0}".format(x2)
print(equation)

