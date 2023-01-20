mode=input("select mode 1 for scientific and 2 for programmer: ")
if mode == '1':
    print("you are on scientific Mode you can use these operators + - * / % ^\n")
    x=int(input("Enter First Operand: "))
    op=input("Enter Operator: ")
    y=int(input("Enter second Operand: "))

    if op == '+':
        print(x+y)
    elif op == '-':
        print(x-y)
    elif op == '*':
        print(x*y)
    elif op == '/':
        print(x/y)
    elif op == '%':
        print(x%y)
    elif op == '^':
        print(pow(x,y))
    else:
        print("not valid operator")
elif mode =='2':
    print("you are on programmer Mode you can use these operators 2 8 16 >> << ~ & | ^  \n")
    x=int(input("Enter First Operand"))
    op=input("Enter Operator")
    if op == '2':
        print(bin(x))
    elif op == '8':
        print(oct(x))
    elif op == '16':
        print(hex(x))
    elif op == '>>' :
        print(x>>1)
    elif op == '<<' :
        print(x<<1)
    elif op == '~' :
        print(~x)
    elif op == '&' :
        y=int(input("Enter second Operand: "))
        print(x & y)
    elif op == '|' :
        y=int(input("Enter second Operand: "))
        print(x | y)
    elif op == '^' :
        y=int(input("Enter second Operand: "))
        print(x ^ y)
    else:
        print("not valid operator")
else :
    print("not valid Mode")

    
    
