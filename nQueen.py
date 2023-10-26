from datetime import datetime
def nQueen(n):
    col=set()
    posdig=set()
    negdig=set()
    
    res=[]
    board=[["0"]*n for row in range(n)]
    def backtrack(r):
        if r==n:
            copy=[" ".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r+c) in posdig or (r-c) in negdig:
                continue
            
            col.add(c)
            posdig.add(r+c)
            negdig.add(r-c)
            board[r][c]="1"
            backtrack(r+1)
            
            col.remove(c)
            posdig.remove(r+c)
            negdig.remove(r-c)
            board[r][c]="0"
    backtrack(0)
    for sol in res:
        for row in sol:
            print(row)
        print()
    print("Total Number of solutions : ", len(res))
start=datetime.now()
n=int(input("Enter the number of queens : "))
print(nQueen(n))

end=datetime.now()
print("Time Complexity : ",end-start)