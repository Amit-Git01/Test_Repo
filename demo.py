import random
import math

def generate_random_numbers(count=10, start=1, end=100):
    """Generate a list of random numbers"""
    return [random.randint(start, end) for _ in range(count)]

def calculate_statistics(numbers):
    """Calculate mean and standard deviation"""
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return {"mean": mean, "std_dev": std_dev}

if __name__ == "__main__":
    data = generate_random_numbers(20)
    print(f"Random numbers: {data}")
    stats = calculate_statistics(data)
    print(f"Statistics: {stats}")