#A
def for_A_pattern(a):
    """
      We are Create a For Loop Patterns by using Star Symboles(*)
      with the Parameters are fellows:
      Parameters:
            Row  : we have define Number of paramaters
            Cols : We have to Provide Number of Columns we need to print Cap pattern A 
    """
    width=(2*a)-1
    n=width//2  
    for i in range(0,a):
        for j in range(0,width+1):
            if (j==n or j==(width-n)or(i==(a//2) and j>n and j<(width-n))):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        n=n-1

    
#A
def while_A_pattern(a):
    #a=int(input("Enter the  number :"))
    b=a+a
    row=0
    while row<a:
        col=0
        while col<b:
            if (row+col==a-1)or (col==row+a-1)or (row==a//2 and col!=0 and col!=1 and col!=b-1 and col!=b-2 and col!=b-3 and col!=b-4 ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
