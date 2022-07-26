#z
class small_alphabits:
    def __init__(self):
        pass
    def for_z(self,z):
        for row in range(z):#6
            for col in range(z):#6
                if (row==0) or (col+row==5) or (row==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

