class solution:
    def pow(self,x,n):
        if n > 0:
            return self.calc(x,n)
        if n < 0:
            x=1/self.calc(x,abs(n))
            return x


    def calc(self,x,n):
        val=x
        while n > 1:
            x*=val
            n-=1
        return x



if __name__ =="__main__":
    soln=solution()
    print(soln.pow(2.000,-2))   