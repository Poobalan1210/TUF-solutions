class solution:
    def search(self,mat,target):
        m=len(mat)
        n=len(mat[0])

        low=0
        high=m*n-1

        while low <= high:
            mid = low+(high-low)//2
            if mat[mid//n][mid%n] == target:
                return True
            if mat[mid//n][mid%n] < target:
                low=mid+1
            else:
                high=mid-1
        return False
            

if __name__ == "__main__":
    soln=solution()
    mat=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target=48
    print(soln.search(mat,target))