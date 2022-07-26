
#G 
b=int(input("Enter the the 7 abo number :"))#G
for row in range(b):
    for col in range(b):
        if (col==0 and row!=0 and row!=b-1 and row!=b-2)or(row==0 and col!=0)or(row==b-2 and col!=0)or(col==b-1 and row>b//2-1)or(row==b//2 and col>1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
