class solution:
    def search(self,mat,target):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==target:
                    return True

        return False


if __name__ =="__main__":
    soln=solution()
    mat=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target=56
    print(soln.search(mat,target))