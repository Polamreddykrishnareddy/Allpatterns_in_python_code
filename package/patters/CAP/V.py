def for_V_pattern(a):
     """
      We are Create a For Loop Patterns by using Star Symboles(*)
      with the Parameters are fellows:
      Parameters:
            Row  : we have define Number of paramaters
            Cols : We have to Provide Number of Columns we need to print Cap pattern A 
    """
     for row in range(a):
        for col in range(a*2+2):
            if (row+col==a+a//2+a%2)or(row==col):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_V_pattern(a):
    row=0
    while row<a:
        col=0
        while col<a+a:
            if (row==col)or(row+col==a+a-2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()

    
