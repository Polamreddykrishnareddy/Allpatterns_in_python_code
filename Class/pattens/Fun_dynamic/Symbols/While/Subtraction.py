    # 6.Subtraction
print("Subtraction")
def Subtraction(a):
    row=0
    while row<a:
        col=0
        while col<a+2:
            if (row==a//2) or (row==a-1)or(col==0 and row>a//2)or(col==a+1 and row>a//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()