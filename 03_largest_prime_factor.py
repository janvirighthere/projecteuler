def largest_prime_factor(number):
    prime_factor = 1
    factor = 2

    while factor <= number / factor:
        if number % factor == 0:
            prime_factor = factor
            number /= factor
        else:
            factor += 1

    if prime_factor < number:
        prime_factor = number

    return prime_factor


print(largest_prime_factor(600851475143))
