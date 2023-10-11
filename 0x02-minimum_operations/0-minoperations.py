def minOperations(n):
    result = 0
    clipboard = 0
    for i in range(2, n + 1):
        while n % i == 0:
            if clipboard == 0:
                clipboard = i
                result += 1
            else:
                clipboard *= i
                result += 1
            n //= i
    return result