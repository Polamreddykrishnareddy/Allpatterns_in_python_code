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
    #B
    def for_B(self,B,b):
        for row in range(B):#7
            for col in range(b):#6
                if (col==0 )or(row==0 and col!=5)or(row==1 and col==5) or (row==2 and  col==5)  or (row==3 and col!=5)  or  (row==6 and col!=5)or (row==4 and col==5)or (row==5 and col==5): 
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #C
    def for_C(self,C):
        for row in range(C):#7
            for col in range(C):#7
                if (row==0 and col==3)or (row==0 and col==4)or (row==0 and col==5) or(row==0 and col==2) or (row==1 and col==1) or (row==2 and col==1) or (row==3 and col==1)or(row==4 and col==3) or(row==4 and col==4)or(row==4 and col==5)or(row==4 and col==2):
                     print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #D
    def for_D(self,D):
        for row in range(D):#6
            for col in range(D):#6
                if (col==0 or col==1 and row!=1 and row!=2 and row!=3 and row!=4)or (col==2 and row!=1 and row!=2 and row!=3 and row!=4) or (col==3 and row!=0 and row!=2 and row!=3  and row!=5) or (col==4 and row!=0 and row!=1 and row!=4  and row!=5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #E
    def for_E(self,E,e):
        for row in range(E):#7
            for col in range(e):#6
                if col==0 or row==0 or row==3 or row==6:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #F
    def for_F(self,F,f):
        for row in range(F):#7
            for col in range(f):#6
                if col==0 or row==0 or row==3:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #G
    def for_G(self,G):
        for row in range(G):#6
            for col in range(G):#6
                if (col==0 and row!=0)or(row==0 and col==1)or(row==0 and col==2) or (row==3 and col!=1) or (col==5 and row!=0 and row!=1 and row!=2) or(row==4 and col==3) or (row==5 and col!=4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #H
    def for_H(self,H,h):
        for  row in range(H):#7
            for col in range(h):#6
                if col==0 or col==5 or row==3 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #I
    def for_I(self,I,i):
        for row in range(6):
            for col in range(7):
                if row==0 or col==3 or row==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #J
    def for_J(self,J,j):
        for row in range(J):#6
            for col in range(j):#7
                if (col==3 or row==0 )or(row==4 and col==1)or (row==5 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #K
    def for_K(self,K,k):
        for row in range(K):#8
            for col in range(k):#9
                if (col==0 or row==col+3)or (col==1 and row==3)or(row==2 and col==2)or (row==1 and col==3) or (row==0 and col==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #L
    def for_L(self,L,l):
        for row in range(L):#8
            for col in range(l):#6
                if col==0 or row==7:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #M
    def for_M(self,M,m):
        for row in range(M):#7
            for col in range(m):#11
                if (col==0 )or (row==3 and col==7)or (row==2 and col==8)or (row==1 and col==9)or (col==10)or(row==4 and col==6)or(row==1 and col==1)or(row==2 and col==2)or(row==3 and col==3)or(row==4 and col==4)or (row==5 and col==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #N
    def for_N(self,N):
        for row in range(N):
            for col in range(N):
                if (col==0) or (col==row) or (col==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #O
    def for_O(self,O):
        for row in range(O):#5
            for col in range(O):#5
                if (row==0 and col==1 ) or (row==0 and col==3 ) or (row==0 and col==2 ) or (col==0 and row!=0 and row!=4)or (row==4 and col!=0 and col!=4)or (col==4 and row!=0 and row!=4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #P
    def for_P(self,P,p):
        for row in range(P):#11
            for col in range(p):#7
                if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #Q
    def for_Q(self,Q):
        for row in range(Q):#8
            for col in range(Q):#8
                if (col==1 and row==0)or (col==2 and row==0)or (col==3 and row==0)or (col==4 and row==1)or (col==4 and row==2)or (col==4 and row==3)or (col==5 and row==5)or (col==6 and row==6)or (col==1 and row==4)or (col==2 and row==4)or (col==3 and row==4)or (col==4 and row==4)or (col==0 and row==1)or (col==0 and row==2)or (col==0 and row==3)or (col==3 and row==3)or (col==2 and row==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #R
    def for_R(self,R,r):
        for row in range(R):#11
            for col in range(r):#6
                if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1)or (row==col+5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #S
    def for_S(self,S,s):
        for row in range(S):#9
            for col in range(s):#7
                if (row==0 and col==3)or(row==0 and col==4)or (row==0 and col==5) or(row==0 and col==2) or (row==1 and col==1) or (row==2 and col==1) or (row==3 and col==1)or(row==4 and col==3) or(row==4 and col==4)or(row==4 and col==5)or(row==4 and col==2) or (row==5 and col==6) or (row==6 and col==6) or (row==7 and col==6) or (row==8 and col==5)or (row==8 and col==4)or (row==8 and col==3)or (row==8 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #T
    def for_T(self,T):
         for row in range(T):#7
            for col in range(T):#7
                if col==3 or row==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #U
    def for_U(self,S,s):
        for row in range(S):#6
            for col in range(s):#10
                if ( col==0 and row!=4 and row!=5) or(col==4 and row!=4 and row!=5)or (row==4 and col==1 ) or (row==4 and col==2)or (row==4 and col==3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #V
    def for_V(self,V,v):
        for row in range(V):#6
            for col in range(v):#15
                if (col==row)or (col+row==10):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #W
    def for_W(self,W,w):
        for row in range(W):#6
            for col in range(w):#18
                if (col==row)or (row==4 and col==6)or (row==3 and col==7)or (row==2 and col==8)or (row==3 and col==9)or (row==4 and col==10)or (row==5 and col==11) or(row+col==16):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #X
    def for_X(self,X):
        for row in range(X):#11
            for col in range(X):#11
                if (row==col) or (row==0 and col==10)or (row==1 and col==9)or (row==2 and col==8)or (row==3 and col==7)or (row==4 and col==6)or (row==6 and col==4)or (row==7 and col==3)or (row==8 and col==2)or (row==9 and col==1)or (row==10 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        #Y
    def for_Y(self,Y):
        for row in range(Y):#11
            for col in range(Y):#11
                if (row==col and col<6)or(col==5 and row>5) or (row==0 and col==10)or (row==1 and col==9)or (row==2 and col==8)or (row==3 and col==7)or (row==4 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
       #Z
    def for_Z(self,Z,z):
        for row in range(Z):#12
            for col in range(z):#10
                if (row==0)or(row+col==9)or (row==9) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 
















