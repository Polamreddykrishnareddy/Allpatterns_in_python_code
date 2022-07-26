#z
class small_alphabets:
    def __init__(self):
        pass
    def z(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 )or (row+col==a-1 ) or(row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
