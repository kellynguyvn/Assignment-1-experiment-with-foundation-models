def find_max(numbers):
    return max(numbers)

# Example usage and performance comparison
import timeit
import random

# Generate a large list of random numbers
test_list = [random.randint(1, 1000000) for _ in range(1000000)]

# Original function
def original_find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Time the original function
original_time = timeit.timeit(lambda: original_find_max(test_list), number=10)

# Time the optimized function
optimized_time = timeit.timeit(lambda: find_max(test_list), number=10)

print(f"Original function time: {original_time:.6f} seconds")
print(f"Optimized function time: {optimized_time:.6f} seconds")
print(f"Speedup: {original_time / optimized_time:.2f}x")