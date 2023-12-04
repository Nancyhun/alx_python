def is_prime(number):
    factors = set()
    for i in range(1, number+1):
        if number % i == 0:
            factors.add(i)
    if len(factors) != 2: # prime numbers have only two elements in their set. So return false if it doesnt
        return False
    
    return True

print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(20))