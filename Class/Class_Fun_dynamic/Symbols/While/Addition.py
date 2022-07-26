    
class symbols:
    def __init__(self):
        pass    
    print("Addison")
    def Addison(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==a//2)or(col==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

