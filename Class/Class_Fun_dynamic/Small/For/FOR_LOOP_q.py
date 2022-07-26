#q
class Small_alphabets:
    def __init__(self):
        pass
    def q(self,a):
        for row in range(a+3):
            for col in range(a):
                if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
