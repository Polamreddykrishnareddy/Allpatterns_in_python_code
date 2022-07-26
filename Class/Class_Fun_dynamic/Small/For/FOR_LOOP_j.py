#j
class Small_alphabets:
    def __init__(self):
        pass
    def j(self,a):
        b=a+3
        for row in range(b):
            for col in range(a):
                if  (col==a//2) or (row==0)or (row-col==a):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
