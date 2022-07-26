class small_alphabits:
    def __init__(self):
        pass
    #a
    def while_a(self,a):
        row=0
        while row<a:#10
            col =0
            while col<a:#10
                if (col==5 and row!=0 and row!=1) or(row==2 and col==2)or (row==1 and col==4) or (row==1 and col==3) or (row==5 and col==4) or (row==5 and col==3) or (row==6 and col==2) or (row==7 and col==2) or (row==8 and col==3)or (row==8 and col==4) or (row==9 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #b
    def while_b(self,b,B):
        row=0
        while row<b:#11
            col=0
            while col<B:#5
                if (col==0)or (row==6 and col==1)or (row==6 and col==2)or (row==6 and col==3)or (row==7 and col==4)or (row==8 and col==4)or (row==9 and col==4)or(row==10 and col==3)or(row==10 and col==2)or(row==10 and col==1) :

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #c
    def while_c(self,c): 
        row=0
        while row<c:#7
            col =0
            while col<c:#7
                if (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()



    #d
    def while_d(self,d,D):
        row=0
        while row<d:#10
            col =0
            while col<D:#7
                if (col==6 and row!=9)or (row==9 and col!=6 and col!=0)or (row==5 and col!=0) or (row==6 and col==0)or (row==7 and col==0)or (row==8 and col==0):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #e
    def while_e(self,e):
        row=0
        while row<e:#7
            col =0
            while col<e:#7
                if  (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0) or (row==2 and col==1)or (row==2 and col==2)or (row==2 and col==5)or  (row==2 and col==3)or (row==2 and col==4)or (row==1 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #f
    def while_f(self,f,F):
        row=0
        while row<f:#9
            col =0
            while col<F:#10
                if (col==4 and row!=0)or (row==0 and col==5)or (row==0 and col==6)or (row==0 and col==7)or (row==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #g
    def while_g(self,g):
        row=0
        while row<g:#10
            col =0
            while col<g:#10
                if (col==9 and row!=0)or (row==9 and col==8)or (row==8 and col==7) or (row==0 and col==8)or (row==0 and col==7)or (row==0 and col==6)or (row==0 and col==5) or (row==1 and col==4)or (row==2 and col==4)or (row==3 and col==4)or (row==4 and col==5) or (row==4 and col==6) or (row==4 and col==7) or (row==4 and col==8):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #h
    def while_h(self,h,H):
        row=0
        while row<h:#11
            col =0
            while col<H:#10
                if (col==0) or (row==5 and col==1)or(row==5 and col==2)or(row==5 and col==3)or(row==5 and col==4)or(row==6 and col==5)or(row==7 and col==5)or(row==8 and col==5)or(row==9 and col==5)or(row==10 and col==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #i
    def while_i(self,i):
        row=0
        while row<i:#10
            col =0
            while col<i:#10
                if (col==5 and row!=1)or (col==6 and row!=1):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #j
    def while_j(self,j):
        row=0
        while row<j:#10
            col=0
            while col<j:#10
                if (col==5 and row!=1)or (row==8 and col==4)or (row==7 and col==3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #k
    def while_k(self,k,K):
        row=0
        while row<k:#15
            col =0
            while col<K:#20
                if (col==0)or (row==col+8)or (row==8 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==5)or (row==4 and col==6) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #l
    def while_l(self,l):
        row=0
        while row<l:#10
            col =0
            while col<l:#10
                if col==5 or col==6:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #m
    def while_m(self,m,M):
        row=0
        while row<m:#5
            col =0
            while col<M:#10
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<M//2 and col>1)or (col==M//2 and row>0)or (row==0 and col>M//2 and col<M-1)or(col==M-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #n
    def while_n(self,n,N):
        row=0
        while row<n:#5
            col =0
            while col<N:#10
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<N//2 and col>1)or (col==N//2 and row>0)or (row==0 and col>N//2 and col<n):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #o
    def while_o(self,o):
        row=0
        while row<o:#5
            col =0
            while col<o:#5
                if (row==0 and col!=0 and col!=4) or (col==0 and row!=0 and row!=4) or (row==4 and col!=0 and col!=4) or (col==4 and row!=0 and row!=4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #p
    def while_p(self,p,P):
        row=0
        while row<p:#11
            col =0
            while col<P:#7
                if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


    #q
    def while_q(self,q,Q):
        row=0
        while row<q:#13
            col =0
            while col<Q:#6
                if (col==5 or row==0 and col!=0 and col!=6 and col!=7) or (row==1 and col==0)or (row==2 and col==0)or (row==3 and col==0)or (row==4 and col==0) or (row==5 and col!=0 and col!=6 and col!=7) or (row==11 and col==6) or (row==10 and col==7):#p

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #r
    def while_r(self,r):
        row=0
        while row<r:#10
            col =0
            while col<r:#10
                if (col==1 and row!=0 )or(row==0 and col==0) or (row==1 and col==2)or (row==1 and col==3)or (row==1 and col==4)or (row==1 and col==5) or (row==2 and col==6)or (row==3 and col==7):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row +=1
            print()

    #s
    def while_s(self,s,S):
        row=0
        while row<s:#10
            col =0
            while col<S:#8
                if (row==0 and col!=0 and col!=6) or (row==1 and col==0 or row==1 and col==6)or (row==2 and col==0)or (row==3 and col==1)or (row==4 and col==2)or (row==5 and col==3)or (row==6 and col==4)or (row==7 and col==5) or (row==8 and col==6)  or (row==8 and col!=0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #t
    def while_t(self,t):
        row=0
        while row<t:#9
            col =0
            while col<t:#9
                if (col==4) or (row==2) or (row==8 and col!=0 and col!=1 and col!=2 and col!=3):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #u
    def while_u(self,u,U):
        row=0
        while row<u:#7
            col =0
            while col<U:#8
                if (col==0 and row!=6) or (col==5  and row!=6 ) or (row==6 and col==1) or (row==6 and col==2) or (row==6 and col==3) or (row==6 and col==4)or(row==6 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #v
    def while_v(self,v,V):
        row=0
        while row<v:#7
            col =0
            while col<V:#15
                if (col+row==12) or (row==col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #w
    def while_w(self,w,W):
        row=0
        while row<w:#7
            col =0
            while col<W:#30
                if (col+row==12) or (row==col) or(col==row+12) or (col+row==24):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

    #x
    def while_x(self,x,X):
        row=0
        while row<x:#10
            col=0
            while col<X:#11
                if col==row or row+col==8:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #y
    def while_y(self,y,Y):
        row=0
        while row<y:#10
            col=0
            while col<Y:#9
                if (row+col==8 ) or (row==0 and col==0) or (row==1 and col==1)or (row==2 and col==2)or (row==3 and col==3)or (row==4 and col==4) or (row==7 and col==0)or(row==6 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
    #z
    def while_z(self,z):
        row=0
        while row<z:#10
            col=0
            while col<z:#10
                if (row==0) or (col+row==8) or (row==8):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()








