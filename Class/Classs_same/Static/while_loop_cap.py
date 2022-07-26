class capital_alphabets:
    def __init__(self):
        pass    
    #A
    def while_A(self,a,b):
        row=0
        while row<a:#5
            col=0
            while col<b:#10
                if (row+col==a-1)or (col==row+a-1)or (row==a//2 and col>a//2-1 and col<a+a//2): 
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
    #B
    def while_B(self,B,b):
        row=0
        while row<B:#7
            col =0
            while col<b:#6
                if (col==0)or(row==0 and col!=5)or(row==1 and col==5) or (row==2 and  col==5)  or (row==3 and col!=5)  or  (row==6 and col!=5)or (row==4 and col==5)or (row==5 and col==5): 
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #C
    def while_C(self,C):
        row=0
        while row<C:#7
            col =0
            while col<C:#7
                if (row==0 and col==3)or (row==0 and col==4)or (row==0 and col==5) or(row==0 and col==2) or (row==1 and col==1) or (row==2 and col==1) or (row==3 and col==1)or(row==4 and col==3) or(row==4 and col==4)or(row==4 and col==5)or(row==4 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #D
    def while_D(self,D):
        row=0
        while row<D:#6
            col =0
            while col<D:#6
                if (col==0 or col==1 and row!=1 and row!=2 and row!=3 and row!=4)or (col==2 and row!=1 and row!=2 and row!=3 and row!=4) or (col==3 and row!=0 and row!=2 and row!=3  and row!=5) or (col==4 and row!=0 and row!=1 and row!=4  and row!=5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
        #E
    def while_E(self,E,e):
        row=0
        while row<E:#7
            col =0
            while col<e:#6
                if col==0 or row==0 or row==3 or row==6:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #F
    def while_F(self,F,f):
        row=0
        while row<F:#7
            col =0
            while col<f:#4
                if col==0 or row==0 or row==3:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #G
    def while_G(self,G):
        row=0
        while row<G:#6
            col =0
            while col<G:#6
                if (col==0 and row!=0)or(row==0 and col==1)or(row==0 and col==2) or (row==3 and col!=1) or (col==5 and row!=0 and row!=1 and row!=2) or(row==4 and col==3) or (row==5 and col!=4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


    #H
    def while_H(self,H,h):
        row=0
        while row<H:#7
            col =0
            while col<h:#6
                if col==0 or col==5 or row==3  :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #I
    def while_I(self,I,i):
        row=0
        while row<I:#6
            col =0
            while col<i:#7
                if row==0 or col==3 or row==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


    #J
    def while_J(self,J,j):
        row=0
        while row<J:#6
            col =1
            while col<j:#7
                if (col==3 or row==0 ) or (row==4 and col==1)or (row==5 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


    #K
    def while_K(self,K,k):
        row=0
        while row<K:#8
            col =0
            while col<k:#9
                if (col==0 or row==col+3)or (col==1 and row==3)or(row==2 and col==2)or (row==1 and col==3) or (row==0 and col==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


    #L
    def while_L(self,L,l):
        row=0
        while row<L:#8
            col =0
            while col<l:#6
                if col==0 or row==7:            
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
        #M
    def while_M(self,M,m):
        row=0
        while row<M:#7
            col =0
            while col<m:#11
                if (col==0 )or (row==3 and col==7)or (row==2 and col==8)or (row==1 and col==9)or (col==10)or(row==4 and col==6)or(row==1 and col==1)or(row==2 and col==2)or(row==3 and col==3)or(row==4 and col==4)or (row==5 and col==5):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #N
    def while_N(self,N):
        row=0
        while row<N:#6
            col =0
            while col<N:#6
                if (col==0) or (col==row) or (col==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


        #O
    def while_O(self,O):
        row=0
        while row<O:#5
            col =0
            while col<O:#5
                if (row==0 and col==1 ) or (row==0 and col==3 ) or (row==0 and col==2 ) or (col==0 and row!=0 and row!=4)or (row==4 and col!=0 and col!=4)or (col==4 and row!=0 and row!=4):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #P
    def while_P(self,P,p):
        row=0
        while row<P:#11
            col =0
            while col<p:#7
                if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
        #Q
    def while_Q(self,Q):
        row=0
        while row<Q:#8
            col =0
            while col<Q:#8
                if (col==1 and row==0)or (col==2 and row==0)or (col==3 and row==0)or (col==4 and row==1)or (col==4 and row==2)or (col==4 and row==3)or (col==5 and row==5)or (col==6 and row==6)or (col==1 and row==4)or (col==2 and row==4)or (col==3 and row==4)or (col==4 and row==4)or (col==0 and row==1)or (col==0 and row==2)or (col==0 and row==3)or (col==3 and row==3)or (col==2 and row==2):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

        #R
    def while_R(self,R,r):
        row=0
        while row<R:#11
            col =0
            while col<r:#6
                if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1)or (row==col+5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

        #S
    def while_S(self,S,s):
        row=0
        while row<S:#9
            col =0
            while col<s:#7
                if (row==0 and col==3)or (row==0 and col==4)or (row==0 and col==5) or(row==0 and col==2) or (row==1 and col==1) or (row==2 and col==1) or (row==3 and col==1)or(row==4 and col==3) or(row==4 and col==4)or(row==4 and col==5)or(row==4 and col==2) or (row==5 and col==6) or (row==6 and col==6) or (row==7 and col==6) or (row==8 and col==5)or (row==8 and col==4)or (row==8 and col==3)or (row==8 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #T
    def while_T(self,T):
        row=0
        while row<T:#7
            col =0
            while col<T:#7
                if col==3 or row==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

        #U
    def while_U(self,U,u):
        row=0
        while row<U:#6
            col =0
            while col<u:#10
                if ( col==0 and row!=4 and row!=5) or(col==4 and row!=4 and row!=5)or (row==4 and col==1 ) or (row==4 and col==2)or (row==4 and col==3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #V
    def while_V(self,V,v):
        row=0
        while row<V:#6
            col =0
            while col<v:#15
                if (col==row)or (col+row==10):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #W
    def while_W(self,W,w):
        row=0
        while row<W:#6
            col =0
            while col<w:#18
                if (col==row)or (row==4 and col==6)or (row==3 and col==7)or (row==2 and col==8)or (row==3 and col==9)or (row==4 and col==10)or (row==5 and col==11) or(row+col==16):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
        #X
    def while_X(self,X):
        row=0
        while row<X:#11
            col =0
            while col<X:#11
                if (row==col) or (row==0 and col==10)or (row==1 and col==9)or (row==2 and col==8)or (row==3 and col==7)or (row==4 and col==6)or (row==6 and col==4)or (row==7 and col==3)or (row==8 and col==2)or (row==9 and col==1)or (row==10 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #Y
    def while_Y(self,Y):
        row=0
        while row<Y:#11
            col =0
            while col<Y:#11
                if (row==col and col<6)or(col==5 and row>5) or (row==0 and col==10)or (row==1 and col==9)or (row==2 and col==8)or (row==3 and col==7)or (row==4 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
        #Z
    def while_Z(self,Z,z):
        row=0
        while row<Z:#12
            col =0
            while col<z:#10
                if (row==0)or(row+col==9)or (row==9) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()















































            
            
