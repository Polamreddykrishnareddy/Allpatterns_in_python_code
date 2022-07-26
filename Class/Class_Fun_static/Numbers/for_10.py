#10
class numbers:
    def __init__(self):
        pass
    def for_10(self,a,b):
        for row in range(a):#10
            for col in range(b):#16
                if (col==5 ) or(row==1 and col==4)or(row==2 and col==3) or (row==3 and col==2)or (row==9 and col!=11 and col!=12 and col!=13 and col!=14 and col!=15 ) or (row==2 and col==7)or (row==3 and col==7) or (row==4 and col==7)or (row==5 and col==7)or(row==6 and col==7)or(row==6 and col==7) or (row==2 and col==14) or (row==3 and col==14) or (row==4 and col==14) or (row==5 and col==14)or(row==6 and col==14) or (row==1 and col==8) or (row==1 and col==9)or (row==1 and col==10)or (row==1 and col==11)or (row==1 and col==12)or (row==1 and col==13) or (row==7 and col==8)or (row==7 and col==9)or (row==7 and col==10)or (row==7 and col==11)or(row==7 and col==12)or (row==7 and col==13):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


