# method that return size of max perfect set
def get_max_perfect_set(n, lst):
    # sort the lst in increasing order
    lst.sort()
    
    # create a dp array of size n and initialise values with 1
    dp = [1]*n
    
    # traverse lst from i=0 to end of lst
    for i in range(n):
        # traverse lst from j=i-1 to 0
        for j in range(i-1, -1, -1):
            # if following condition passes, then update dp[i] with max(dp[i], dp[j]+1)
            if lst[j]*lst[j] == lst[i]:
                dp[i] = max([dp[i], 1+dp[j]])
    
    # if max(dp) == 1, then return -1
    if max(dp) == 1 :
        return -1
    
    # else return max(dp) which is the max perfect set size
    return max(dp)
    
    
# testcases
print(get_max_perfect_set(5, [625, 4, 2, 5, 25]))
print(get_max_perfect_set(4, [7, 4, 8, 9]))