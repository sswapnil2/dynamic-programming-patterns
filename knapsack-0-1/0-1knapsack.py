# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Question
#
#  The goal is to get the maximum profit from the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.
#
#
#Items: { Apple, Orange, Banana, Melon }
#Weights: { 2, 3, 1, 4 }
#Profits: { 4, 5, 3, 7 }
#Knapsack capacity: 5
#
#

# Problem can be solved using two approaches

# 1 recursive approach 

# brute force solution

#  complexity O(2^n)
def solve_recursive(weights, profits, capacity, index):
    
    if capacity <= 0 or index >= len(profits):
        return 0
        
    profit_1 = 0
    if weights[index] <= capacity:
        profit_1 = profits[index] + solve_recursive(weights, profits, capacity - weights[index], index + 1)
    
    profit_2 = solve_recursive(weights, profits, capacity, index + 1)
    
    return max(profit_1, profit_2)
    

def solve_knapsack(weights, profits, capacity):
    return solve_recursive(weights, profits, capacity, 0)
    
    
# because it contains repetative problems 
# we can use dp

# time complxity is O(n*c)
def solve_recursive(dp, weights, profits, capacity, index):
    
    if capacity <= 0 or index >= len(profits):
        return 0
    
    if not dp[index][capacity]:
        profit_1 = 0
        if weights[index] <= capacity:
            profit_1 = profits[index] + solve_recursive(dp, weights, profits, capacity - weights[index], index + 1)
        
        profit_2 = solve_recursive(dp, weights, profits, capacity, index + 1)
        
        dp[index][capacity] = max(profit_1, profit_2)
    return dp[index][capacity]

def solve_knapsack(weights, profits, capacity):
    dp = [[0 for j in range(capacity + 1)] for i in range(len(profits))]
    return solve_recursive(dp, weights, profits, capacity, 0)


    
# bottom up approach
def solve_knapsack(weights, profits, capacity):
    
    if capacity == 0:
        return 0
    # create dp
    dp = [[0 for j in range(capacity + 1)] for i in range(len(profits))]
    
    # for 1st index the maximum value will be the value itself
    for c in range(1, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    
    # loop over all the capacity and weights
    for i in range(1, len(weights)):
        for c in range(1, capacity + 1):
            
            # only two ways we have
            # either include current index or do not include current index
            profit_1 = 0
            if weights[i] <= c:
                profit_1 = profits[i] + dp[i-1][c - weights[i]]
            
            dp[i][c] = max(dp[i-1][c], profit_1)
    
    return dp[len(profits) -1][capacity]
    

# we can reduce the space complexity in above approach
# if we look at ir carefully we only need the previous indexes values
# for calculating the current values
def solve_knapsack(weights, profits, capacity):
    
    if capacity == 0:
        return 0
    # create dp
    dp = [0 for j in range(capacity + 1)]
    
    # for 1st index the maximum value will be the value itself
    for c in range(1, capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]
    
    # loop over all the capacity and weights
    for i in range(1, len(weights)):
        current = [0 for _ in range(capacity + 1)]
        for c in range(1, capacity + 1):
            
            # only two ways we have
            # either include current index or do not include current index
            profit_1 = 0
            if weights[i] <= c:
                profit_1 = profits[i] + dp[c - weights[i]]
            
            current[c] = max(dp[c], profit_1)
        dp = current
    
    return dp[capacity]   



print(solve_knapsack([1, 2, 3, 5], [1, 6, 10, 16], 7))
print(solve_knapsack([1, 2, 3, 5], [1, 6, 10, 16],  6))
    
    
	
