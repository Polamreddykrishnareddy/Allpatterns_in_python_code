#e 
a=int(input("Enter the 6 or 6Up number :"))
for row in range(a):
    for col in range(a):
        if (row==0 and col>0 and col<a-1)or(row==a//2-1 and col<a-1) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0)or (col==a-1 and row>0 and row<a//2-1):#(col-row==a//2 and row<a//2-1)  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()