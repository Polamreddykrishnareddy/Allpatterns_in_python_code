#13. Greater than
print("Greater than")
def Greater_than(a):
    for row in range(a):
        for col in range(a):
            if  (col-row==a//2)or(col+row==a//2+a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        