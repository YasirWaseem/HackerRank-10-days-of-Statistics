// we have to complete this function
def weightedMean(X, W):
    # Write your code here
    my_list = []
    for i in range(len(X)):
        my_list.append(X[i] * W[i])
        
    my_listSum = sum(my_list)
    WSum = sum(W)
    
    res = my_listSum / WSum
    
    res = round(res, 1)
    print(res)
