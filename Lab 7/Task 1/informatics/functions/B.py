def power(a, n):
    if n == 0:
        return 1
    half_power = power(a, n // 2)
    if n % 2 == 0:
        return half_power * half_power
    return half_power * half_power * a