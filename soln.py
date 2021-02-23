def processQuery(n,p,query):        # n is number of processes, p is number of queries and query is an array of all queries

    # WRITE YOUR CODE HERE
    num=[*range(1,n+1)]
    dic = {'A':num,'B':[],'C':[],'D':[],'E':[]}
    for q in query:
        a=q.split()
        val=int(a[1])
        q=list(a[0])
        send = q[0]
        to = q[1]
        dic[send].remove(val)
        dic[to].append(val)
    print("A {}".format(*dic['A']))
    print("B {}".format(*dic['B']))
    print("C {}".format(*dic['C']))
    print("D {}".format(*dic['D']))
    print("E {}".format(*dic['E']))

def main():
    S = input().split()
    n = int(S[0])
    p = int(S[1])
    query = []
    for i in range(p):
        P = input()
        query.append(P)
    processQuery(n,p,query)

main()