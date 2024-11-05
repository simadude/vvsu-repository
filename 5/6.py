import math

# C(k, n) = n! / ((n-k)! * k!)

def C (k, n):
    if k < n:
        return 0
    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

def binom_prob(n, p, k):
    return C(k, n) * math.pow(p, k) * math.pow(1 - p, n - k)