def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create an instance of the Fibonacci generator
fib = fibonacci_generator()

# Generate the Fibonacci sequence up to a certain limit
limit = 10
for _ in range(limit):
    print(next(fib))
