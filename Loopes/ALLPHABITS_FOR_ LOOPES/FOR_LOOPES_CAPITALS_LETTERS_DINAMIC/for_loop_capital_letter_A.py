#A

hight=int(input("Enter the number A alphabit pateran :"))#A
width=(2*hight)-1
n=width//2  
for i in range(0,hight):
    for j in range(0,width+1):
        if (j==n or j==(width-n)or(i==(hight//2) and j>n and j<(width-n))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    n=n-1

  

a=int(input("Enter the number:"))
for row in range(a):
    for col in range(a+a):
        if (row+col==a-1)or (col==row+a-1)or (row==a//2 and col>a//2-1 and col<a+a//2): #col!=b-1 and col!=b-2 and col!=b-3 and col!=b-4 and col!=b-5 ) and col<4:
  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    