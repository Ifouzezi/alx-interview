def minOperations(n):
    if n == 1:
        return 0  # Already have 1 'H', so no operations needed.

    # Initialize an array to store the minimum operations needed for each index.
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')  # Initialize to a large value.

        for j in range(1, i):
            if i % j == 0:  # If i is divisible by j.
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

# Example usage:
n = 9
print(minOperations(n))  # Output: 6