#f
def f(a):
    b=a+3
    for row in range(b):
        for col in range(a):
            if (col==a//2-1 and row>0)or (row==b//2) or row==0 and col>a//2-1 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

