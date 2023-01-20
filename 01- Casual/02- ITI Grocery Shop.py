total=0
list=['banana', 'apple', 'tomato']
cost=[15, 10, 5]
ex=0
operation = 1
while ex==0:
    bill=[]
    quantity=[]
    billcost=[]
    triescount=3
    passflag=0
    mode=input("#Welcome to ITI Shop\n	1- Owner\n	2- user\n	0- exit\n	Select Mode: ")

    if mode=='1':
        while triescount>0 and passflag==0 and operation !=0:
            username=input("# Owner mode:\n enter username: ")
            password=input("  enter password: ")
            if password != '123' or username != 'Mahmoud':
                print("incorrect username or password")
                triescount=triescount-1
            else :
                passflag=1
                operation = input("# owner Operation\n	1- show products\n	2- Add product\n	3- change cost\n	4- delete product\n	0 - Exit Mode\n	select operation: ")
                if operation == '1':
                    print("	#show products")
                    print("id     product     cost")
                    for n in range(0,len(cost)):
                        print(n+1, '     ',list[n],'   ', cost[n] )
                elif operation =='2':
                    list.append(input("Enter Product name: "))
                    cost.append(int(input("Enter cost: ")))
                elif operation =='3':
                    x=input("Enter Product name: ")
                    cost[list.index(x)]=int(input("Enter new cost: "))
                elif operation == '4':
                    x=list.index(input("Enter Product name: "))
                    list.pop(x)
                    cost.pop(x)
                else :
                    print("wrong input")
    elif mode == '2':
        operation=1
        while operation!='0':       
            operation = input("# Customer Operation\n	1- show products\n	2- Buy Product\n	3- Print Bill\n	0- Exit Mode\n	select operation: ")
            if operation == '1':
                print("	#show products")
                print("id     product     cost")
                for n in range(0,len(cost)):
                    print(n+1, '     ',list[n],'   ', cost[n] )
            elif operation == '2':
                repeat ='1'
                while repeat == '1':
                    x=list.index(input("Enter Product name: "))
                    bill.append(list[x])
                    billcost.append(cost[x])
                    quantity.append(int(input("enter quantity: ")))
                    repeat=input("enter 1 to choose another product. enter 0 to end operation")
            elif operation == '3':
                print("#print bill")
                print("id     product     quantity     unit cost     total")
                for n in range (0, len(billcost)):
                    total+=billcost[n]*quantity[n]
                    print(n+1,'     ', bill[n], '     ' , quantity[n], '        ', billcost[n], '        ', quantity[n]*billcost[n])
                
                print("==================\n total = ", total, 'EGP')
    elif mode=='0':
        ex=1


            




                

            


