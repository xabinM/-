n = int(input())
nums = list(map(int, input().split()))

def solution(n, nums):
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])

    return max(dp)

print(solution(n, nums))