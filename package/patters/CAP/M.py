def for_M_pattern(a):
     """
      We are Create a For Loop Patterns by using Star Symboles(*)
      with the Parameters are fellows:
      Parameters:
            Row  : we have define Number of paramaters
            Cols : We have to Provide Number of Columns we need to print Cap pattern A 
    """
     c=a+a
     b=c-2
     for row in range(a):
        for col in range(b):
            if (col==0)or(row==col)or(row+col==b>8-1)or (col==b-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_M_pattern(b):
    row=0
    while row<b:
        col=0
        while col<b+b:
            if (col==0)or(row==col)or(row+col==b+b-2)or(col==b+b-2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
