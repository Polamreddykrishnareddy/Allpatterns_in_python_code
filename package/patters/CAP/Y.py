#Y
def for_Y_pattern(a):
     """
      We are Create a For Loop Patterns by using Star Symboles(*)
      with the Parameters are fellows:
      Parameters:
            Row  : we have define Number of paramaters
            Cols : We have to Provide Number of Columns we need to print Cap pattern A 
    """
     if a%2==1:
        for row in range(a):
            for col in range(a*2+2):
                if (row==col and col<a-a//2)+(row+col==a-1 and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
     elif a%2==0:
        for row in range(a):
            for col in range(a*2+2):
                if (row==col and col<a-a//2)+(row+col==a and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
#Y
def while_Y_pattern(a):
    if a%2==1:
        row=0
        while row<a:
            col=0
            while col<a*2+2:
                if (row==col and col<a-a//2)+(row+col==a-1 and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    elif a%2==0:
        row=0
        while row<a:
            col=0
            while col<a*2+2:
                if (row==col and col<a-a//2)+(row+col==a and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
   

