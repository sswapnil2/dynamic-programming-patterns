# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

# Basic idea
# The set can only be divided into two equal partition if 
# the sum of the numbers in the array is even
# if the sum of some numbers in the array is equal to sum/2


# dry run
# input = {1, 2, 3, 4}
# Sum = 1 + 2+ 3 + 4 = 10
# half = 10/2 = 5
# find such numbers in the subset such that their sum is 5
# {1, 4} or {2, 3} if we can find such numbers it means other numbers also sum upto half
# that is subset can be divided into equal partition



# brute force approach
# try all subsets
def solve_recursive(subset, current_sum, index):
    
    # base condition
    if current_sum == 0:
        return True
    
    # base condition
    if current_sum < 0 or index >= len(subset):
        return False
    
    # try out including the first element in the subset
    if subset[index] <= current_sum:
        out = solve_recursive(subset, current_sum - subset[index], index + 1)
        if out:
            return True
    
    # exlude the current index if the the current index is greater than half
    return solve_recursive(subset, current_sum, index + 1)
    
def solve_subset(subset):
    
    if not subset:
        return True
        
    _sum = sum(subset)
    if _sum % 2 == 1:
        return False
    half = _sum // 2
    return solve_recursive(subset, half, 0)


# apprach using dp for recurring problemts
# brute force approach
# try all subsets
def solve_recursive_dp(dp, subset, current_sum, index):
    
    # base condition
    if current_sum == 0:
        return 1
    
    # base condition
    if current_sum < 0 or index >= len(subset):
        return 0
    
    if dp[index][current_sum] == -1:
        # try out including the first element in the subset
        if subset[index] <= current_sum:
            out = solve_recursive_dp(dp, subset, current_sum - subset[index], index + 1)
            if out:
                dp[index][current_sum] = 1
                return dp[index][current_sum]
        
        # exlude the current index if the the current index is greater than half
        dp[index][current_sum] = solve_recursive_dp(dp, subset, current_sum, index + 1)
    
    return dp[index][current_sum]


def solve_subset_with_dp(subset):
    if not subset:
        return True
        
    _sum = sum(subset)
    
    if _sum % 2 == 1:
        return False
    
    half = _sum // 2
    
    dp = [[-1 for j in range(half + 1)] for i in range(len(subset))]
    
    return solve_recursive_dp(dp, subset, half, 0)
    


# solve subset problem using bottom up approach

# there are two cases only
# one to include the current index if current_number <= sum 
# exlclude the current index current_number > sum
def solve_subset_bottom_up(subset):
    if not subset:
        return True
    
    _sum = sum(subset)
    
    if _sum % 2 == 1:
        return False
    half = _sum // 2
    
    # dp
    dp = [[False for c in range(half + 1)] for i in range(len(subset))]
    
    # when sum is 0 then for all index subset is possible
    # for empty subset
    for i in range(len(subset)):
        dp[i][0] = True
    
    # for 1st index
    for c in range(1, half + 1):
        if subset[0] == c:
            dp[0][c] = True
    
    for i in range(1, len(subset)):
        for c in range(1, half + 1):
            
            # if previos 
            if dp[i-1][c]:
                dp[i][c] = dp[i-1][c]
            
            if subset[i] <= c:
                dp[i][c] = dp[i-1][c - subset[i]]
    
    return dp[len(subset)-1][half]
                
        
    
    

    

print(solve_subset([1, 2, 3, 4]))
print(solve_subset_with_dp([1,2,3,4]))
print(solve_subset_bottom_up([1,2,3,4]))
