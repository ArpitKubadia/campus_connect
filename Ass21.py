furniture=["Sofa Set","Dining Table","TV Stand","Cupboard"]
cost=[20000,8500,4599,13920]

req=input("Furniture you want: ")
qty=int(input("Quantity: "))

if req in furniture:
    print("Furniture: ",req)
    print("Amount = ",qty*cost[furniture.index(req)])
else:
    print("Not Found")