class solution:
    def rotate_matrix(self,mat):
        for i in range(len(mat)):
            for j in range(i,len(mat)):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for i in range(len(mat)):
            mat[i]=mat[i][::-1]
        print(mat)
if __name__ =="__main__":
    soln=solution()
    mat=[[1,2,3],[4,5,6],[7,8,9]]
    soln.rotate_matrix(mat)
