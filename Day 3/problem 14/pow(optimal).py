class solution:
    def pow(self,x,n):
        ans=1.0
        nn=n
        if n < 0:
            nn=-1*n
        while nn >0:
            if nn%2==0:
                x*=x
                nn/=2
            else:
                ans=ans*x
                nn-=1
        if n < 0:
            return 1.0/ans
        return ans




if __name__ =="__main__":
    soln=solution()
    print(soln.pow(2.000,10))