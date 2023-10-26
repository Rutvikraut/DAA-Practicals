def knapSack(W, weight, profit, n):
    knapsack=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if weight[i-1]<=W:
                knapsack[i][j]=max(profit[i-1]+knapsack[i-1][j-weight[i-1]],knapsack[i-1][j])
            else:
                knapsack[i][j]=knapsack[i-1][j]
    
    return knapsack[n][W]

profit = [60, 100, 120] 
weight = [10, 20, 30] 
W = 50
n = len(profit) 
print(knapSack(W, weight, profit, n))