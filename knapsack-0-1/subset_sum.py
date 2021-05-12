

# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

#Input: {1, 2, 3, 7}, S=6
# Output: True
# The given set has a subset whose sum is '6': {1, 2, 3}

def solve_recursive(num, sum, index):
   if sum == 0:
      return True
   
   if sum < 0 or index>=len(num):
      return False
   
   if num[index] <= sum:
      out = solve_recursive(num, sum - num[index], index + 1)
      if out:
         return out
   
   return solve_recursive(num, sum, index + 1)

# solution with dp

def solve_recursive_dp(dp, num, sum, index):
   if sum == 0:
      return True
   
   if sum < 0 or index>=len(num):
      return False
   if dp[index][sum] == -1:
      if num[index] <= sum:
         out = solve_recursive_dp(dp, num, sum - num[index], index + 1)
         if out:
            dp[index][sum] =  out
            return dp[index][sum]
      
      dp[index][sum]= solve_recursive_dp(dp, num, sum, index + 1)
   
   return dp[index][sum]


def solve_bottom_up(num, sum):

   # empty subset always has sum 0
   if sum == 0:
      return True 
   
   if not num and sum > 0:
      return False
   
   n = len(num)
   dp = [[False for j in range(sum + 1)] for i in range(n)]

   # for sum = 0 empty subset is always possible
   for i in range(n):
      dp[i][0] = True
   
   # for 1st index subset is only possible when the sum is equal to element
   for c in range(1, sum+1):
      dp[0][c] = num[0] == c
   
   for i in range(1, n):
      for c in range(1, sum+1):

         # without including current element if subset is possible
         # good to go
         if dp[i-1][c]:
            dp[i][c] = dp[i-1][c]

         # if subset is not possible previously try including current 
         # element only if the current element is less than or equal to the sum
         elif num[i] <= c:
            dp[i][c] = dp[i-1][c - num[i]]
   
   return dp[n-1][c]



def can_partition(num, sum):
   #TODO: Write - Your - Code
#    dp = [[-1 for j in range(sum + 1)] for i in range(len(num))]

#    return solve_recursive(num, sum, 0)
#    return True if solve_recursive_dp(dp, num, sum, 0) == 1 else False
   return solve_bottom_up(num, sum)
