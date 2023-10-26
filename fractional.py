def fractionalKnap(w,n,proft,weight):
    arr=[[profit[i],weight[i],profit[i]/weight[i]] for i in range(n)]
    arr=sorted(arr,key=lambda x:x[2], reverse=True)
    totalProf=0
    remainingweight=w
    for item in arr:
        if item[1]<remainingweight:
            totalProf+=item[0]
            remainingweight-=item[1]
        else:
            fraction=remainingweight/item[1]
            totalProf+=item[0]*fraction
            break
    return totalProf
            

profit=[10, 15, 10, 12, 8]
weight=[3, 3, 2, 5, 1]
w=10
n=5
print(fractionalKnap(w,n,profit,weight))