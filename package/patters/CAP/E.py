def for_E_pattern(a):
    for row in range(a):
        for col in range(a):
            if (row==0) or (row==a//2 )or (row==a-1)or(col==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def while_E_pattern(a):
    row=0
    while row<a:
        col=0
        while col<a:
            if (row==0) or (row==a//2 )or (row==a-1)or(col==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()












