class solution:
    def pascal_triangle(self,n):
        output=[]
        if n == 0:
            return output
        output.append([1])

        for i in range(1,n):
            prev_row=output[i-1]
            current_row=[]
            current_row.append(1)

            for j in range(1,i):
                current_row.append(prev_row[j-1]+prev_row[j])
            
            current_row.append(1)
            output.append(current_row)

        print(output)


if __name__ == "__main__":
    soln=solution()
    n=6
    soln.pascal_triangle(n)