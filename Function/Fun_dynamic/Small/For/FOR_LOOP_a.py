#a
def a(b):
    a=3
    for row in range(a+b):
        for col in range(b):
            if(row==0 and col<b-2 and col>0)or(col==b-2 and row>0)or(row==1 and col==0)or(row==(a+b)-2 and col<b-1 and col>0)or(row==(a+b)//2-1 and col<b-1 and col>0)or(col==0 and row>b//2 and row<(a+b)-2) or(row==a+b-1 and col>b-2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()