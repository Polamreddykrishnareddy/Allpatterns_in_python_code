#13. Greater than
print("Greater than")
a=int(input("Enter the  numbers :"))
for row in range(a):
    for col in range(a):
        if  (col-row==a//2)or(col+row==a//2+a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    