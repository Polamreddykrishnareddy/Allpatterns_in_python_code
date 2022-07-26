def for_H_pattern(a):
     """
      We are Create a For Loop Patterns by using Star Symboles(*)
      with the Parameters are fellows:
      Parameters:
            Row  : we have define Number of paramaters
            Cols : We have to Provide Number of Columns we need to print Cap pattern A 
    """
     for row in range(a):
        for col in range(a):
            if (row==a//2) or (col==0) or (col==a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_H_pattern(a):
    row=0
    while row<a:
        col=0
        while col<a:
            if (row==a//2) or (col==0) or (col==a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()


