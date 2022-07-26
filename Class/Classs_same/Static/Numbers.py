class numbers:
    def __init__(self):
        pass   
   #1
    def for_1(self,_1):
        for row in range(_1):#10
            for col in range(_1):#10
                if (col==5) or(row==1 and col==4)or(row==2 and col==3) or (row==3 and col==2)or (row==9):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #2
    def for_2(self,_2):
        for row in range(_2):#10
            for col in range(_2):#10
                if (row==9 )or (col+row==9 and row!=0 and row!=2 and row!=1)or (row==2 and col==6)or (row==1 and col==6)or (row==0 and col==5)or (row==0 and col==4)or (row==0 and col==3)or (row==1 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        #3
    def for_3(self,a,b):
        for row in range(a):#8
            for col in range(b):#6
                if (row==0) or (row==1 and col==4) or (row==2 and col==3)or (row==3 and col==2)or (row==4 and col==3)or (row==5 and col==4) or row==6:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #4
    def for_4(self,a,b):
        for row in range(a):#10
            for col in range(b):#9
                if col+row==6 or row==6 or (col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #5
    def for_5(self,a,b):
        for row in range(a):#10
            for col in range(b):#6
                if row==0 or (row==1 and col==0)or (row==2 and col==0)or (row==3 and col==0)or (row==4 and col==0)or(row==4 and col!=5)or (row==5 and col==5)or (row==6 and col==5)or (row==7 and col==5)or (row==8 and col==4)or (row==8 and col==3)or (row==8 and col==2)or (row==8 and col==1)or (row==8 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


        #6
    def for_6(self,a,b):
        for row  in range(a):#8
            for col in range(b):#6
                if (col==0 and row!=7 and row!=0 and row!=1) or (row==0 and col==2) or(row==1 and col==1)or (row==7 and col==1)or (row==7 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==4)or (row==4 and col==3) or (row==4 and col==1) or (row==4 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #7
    def for_7(self,_7):
        for row in range(_7):#10
            for col in range(_7):#10
                if col+row==6 or row==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()



        #8
    def for_8(self,a,b):
        for row in range(a):#11
            for col in range(b):#6
                if (row==0 and col!=0 and col!=5) or (col==0 and row!=10 and row!=0 and col!=5 and row!=5)or (row==5 and col==1)or (row==5 and col==2)or (row==5 and col==3)or (row==5 and col==4) or(col==5  and row!=10 and row!=5 and row!=0)or (row==10 and col==1)or (row==10 and col==2)or (row==10 and col==3)or (row==10 and col==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #9
    def for_9(self,_9):
        for row in range(_9):#10
            for col in range(_9):#10
                if (col==7 and row!=0) or (row==0 and col==6)or (row==0 and col==5)or (row==0 and col==4)or (row==1 and col==3) or (row==2 and col==3)or (row==3 and col==3)or(row==4 and col==4)or(row==4 and col==5)or (row==4 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #10
    def for_10(self,a,b):
        for row in range(a):#10
            for col in range(b):#16
                if (col==5 ) or(row==1 and col==4)or(row==2 and col==3) or (row==3 and col==2)or (row==9 and col!=11 and col!=12 and col!=13 and col!=14 and col!=15 ) or (row==2 and col==7)or (row==3 and col==7) or (row==4 and col==7)or (row==5 and col==7)or(row==6 and col==7)or(row==6 and col==7) or (row==2 and col==14) or (row==3 and col==14) or (row==4 and col==14) or (row==5 and col==14)or(row==6 and col==14) or (row==1 and col==8) or (row==1 and col==9)or (row==1 and col==10)or (row==1 and col==11)or (row==1 and col==12)or (row==1 and col==13) or (row==7 and col==8)or (row==7 and col==9)or (row==7 and col==10)or (row==7 and col==11)or(row==7 and col==12)or (row==7 and col==13):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

















