    #y
class small_alphabets:
    def __init__(self):
        pass
    def y(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row-col==0 and col<a//2)or (row+col==a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        