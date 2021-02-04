class solution:
    def set_zero(self,mat):
        row=[1]*len(mat)
        col=[1]*len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    row[i] =0
                    col[j]=0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if row[i] == 0:
                    mat[i][j] = 0
                if col[j] == 0:
                    mat[i][j] =0

        print(mat)

if __name__ == "__main__":
    mat=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    soln=solution()
    soln.set_zero(mat)
    