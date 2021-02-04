class solution:
    def set_zero(self,mat):
        col=True

        for i in range(len(mat)):
            if mat[i][0] == 0:
                col=False
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    mat[i][0] = mat[0][j] =0

        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,0,-1):
                if mat[i][0] == 0 or mat[0][j]==0:
                    mat[i][j]=0
            if col is False:
                mat[i][0]=0

        print(mat)





if __name__ == "__main__":
    soln=solution()
    mat=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    soln.set_zero(mat)