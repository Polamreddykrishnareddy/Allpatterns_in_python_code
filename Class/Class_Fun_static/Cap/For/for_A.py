class capital_alphabets:
    def __init__(self):
        pass    
    def for_A(self,A,a):
        for row in range(A):#7
            for col in range(a):#5
                if ((col==0 or col==4) and row!=0) or ((row==0 or row==3)and (col>0 and col<4)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
