class solution:
    def next_permutation(self,n):
        length=len(n)
        pointer=length-2
        
        # less than 2 just reverse 
        if length <=2:
            return n.reverse()
        
        #find the end of the descending order
        while pointer >=0 and n[pointer] > n[pointer+1]:
            pointer-=1
        
        #if there is no break point 
        if pointer == -1:
            return n.reverse()

        # swap the nodes that is greater than the breakpoint
        for i in range(length-1,pointer,-1):
            if n[i] > n[pointer]:
                n[i],n[pointer]=n[pointer],n[i]
                break

        # reverse the list items after the breakpoint
        n[pointer+1:]=reversed(n[pointer+1:])
        print(n) 




if __name__ =="__main__":
    soln=solution()
    n=[1,2,3]
    soln.next_permutation(n)

# video link https://www.youtube.com/watch?v=4wlBBRo4tYY