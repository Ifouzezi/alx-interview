def minOperations(n):
    if n < 2:
        return n  # 0 operations needed for n = 0 and n = 1


    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


    def get_smallest_prime_factor(x):
        for i in range(2, x + 1):
            if x % i == 0 and is_prime(i):
                return i

    operations = 0
    while n > 1:
        smallest_prime = get_smallest_prime_factor(n)
        if smallest_prime == 0:
            return 0  # Impossible to achieve 'n' H characters
        while n % smallest_prime == 0:
            n //= smallest_prime
        operations += smallest_prime
    return operations

# Example usage:
n = 18
result = minOperations(n)
if result == 0:
    print("Impossible to achieve", n, "H characters.")
else:
    print("Fewest number of operations to achieve", n, "H characters:", result)
