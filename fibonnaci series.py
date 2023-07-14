def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
num_terms = 10
fib_sequence = []
for i in range(num_terms):
    fib_sequence.append(fibonacci(i))
    
print(f"Fibonacci sequence of {num_terms} terms:")
print(fib_sequence)
