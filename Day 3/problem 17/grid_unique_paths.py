class solution:
    def grid_unique_paths(self,i,j,m,n):
        if i==m-1 and j == n-1 :return 1
        if i>=m or j>=n:return 0
        else: return self.grid_unique_paths(i+1,j,m,n) + self.grid_unique_paths(i,j+1,m,n)

if __name__ =="__main__":
    soln=solution()
    m,n=3,7
    print(soln.grid_unique_paths(0,0,m,n))