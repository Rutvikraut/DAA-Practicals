import time

# Function to calculate the nth Fibonacci number using recursion
def fibonacci_recursive(n, depth=0):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        if depth == 0:
            print("Starting recursion...")
        result = (
            fibonacci_recursive(n - 1, depth + 1) +
            fibonacci_recursive(n - 2, depth + 1)
        )
        if depth == 0:
            print("Recursion finished.")
        return result

# Function to count the number of recursive calls
def count_recursive_calls(fn):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return fn(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

# Apply the decorator to the recursive function
fibonacci_recursive = count_recursive_calls(fibonacci_recursive)

n = int(input("Enter value of n (nth Fibonacci number): "))

# Start measuring execution time
start_time = time.time()
result = fibonacci_recursive(n, 0)
end_time = time.time()

if isinstance(result, int):
    print(f"Fibonacci Number: {result}")

# Calculate and print execution time
elapsed_time = end_time - start_time
print(f"Execution Time: {elapsed_time:.6f} seconds")

# Estimate stack depth based on the actual number of recursive calls
# This provides a more accurate estimate of stack depth
stack_depth = fibonacci_recursive.call_count
print(f"Estimated Stack Depth: {stack_depth}")
