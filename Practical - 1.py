def calculate_mean(numbers):
 return sum(numbers) / len(numbers)
def calculate_median(numbers):
 numbers.sort()
 n = len(numbers)
 middle = n // 2
 return (numbers[middle - 1] + numbers[middle]) / 2 if n % 2 == 0 else numbers[middle]
def calculate_standard_deviation(numbers):
 mean = calculate_mean(numbers)
 variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
 return variance ** 0.5
def calculate_mode(numbers):
 from collections import Counter
 frequency = Counter(numbers)
 max_count = max(frequency.values())
 return [key for key, value in frequency.items() if value == max_count]
# Input and Execution
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Mean: {calculate_mean(numbers)}")
print(f"Median: {calculate_median(numbers)}")
print(f"Standard Deviation: {calculate_standard_deviation(numbers)}")
print(f"Mode: {calculate_mode(numbers)}")