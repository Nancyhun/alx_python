def fibonacci_sequence(n):
    sequence = [0]
    n1, n2 = 0, 1

    if n == 0:
        return []
    
    elif n == 1:
        return [0] # because we start counting from zero not one
    
    for i in range(n-1):
        sequence.append(n2)
        nth = n1 +  n2
        n1 = n2
        n2 = nth
          
    return sequence

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
