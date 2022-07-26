    #t
class small_alphabets:
    def __init__(self):
        pass
    def t(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==a//2)or(row==a//2-1)or(row==a-1 and col>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
