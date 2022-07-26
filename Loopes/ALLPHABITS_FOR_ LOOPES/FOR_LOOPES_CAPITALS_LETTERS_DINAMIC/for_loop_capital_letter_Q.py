#Q 
a=int(input("Enter the number only 6 or 7:"))#Q
for row in range(a):
    for col in range(a):
        if (row==0 and col!=0 and col!=a-2 and col!=a-1) or (row==a-2 and col!=0 and col!=a-1) or (col==0  and row!=0 and row<a-2) or (col==a-2 and row!=0 and row!=a-1)or (row==a-3 and col==a-3 ) or(row==a-4 and col==a-4)or(row==a-1 and col==a-1):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  