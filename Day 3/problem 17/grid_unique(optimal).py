class solution:
    def unique_paths(self,m,n):
        total=m+n-2
        choose=min(m,n)-1
        
        product=1

        for i in range(choose):
            product=product*total/(i+1)
            total-=1
        print(int(product))





if __name__ =="__main__":
    soln=solution()
    soln.unique_paths(2,3)