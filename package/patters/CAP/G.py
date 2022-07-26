
#G 
def for_G_pattern(b):
     """
      We are Create a For Loop Patterns by using Star Symboles(*)
      with the Parameters are fellows:
      Parameters:
            Row  : we have define Number of paramaters
            Cols : We have to Provide Number of Columns we need to print Cap pattern A 
    """
     for row in range(b):
        for col in range(b):
            if (col==0 and row!=0 and row!=b-1 and row!=b-2)or(row==0 and col!=0)or(row==b-2 and col!=0)or(col==b-1 and row>b//2-1)or(row==b//2 and col>1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def while_G_pattern(b):
    row=0
    while row<b:
        col=0
        while col<b:
            if (col==0 and row!=0 and row!=b-1 and row!=b-2)or(row==0 and col!=0)or(row==b-2 and col!=0)or(col==b-1 and row>b//2-1)or(row==b//2 and col>1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()

