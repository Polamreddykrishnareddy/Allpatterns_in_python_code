    #Z
class capital_alphabets:
    def __init__(self):
        pass
    def for_Z(self,Z,z):
        for row in range(Z):#12
            for col in range(z):#10
                if (row==0)or(row+col==9)or (row==9) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 


