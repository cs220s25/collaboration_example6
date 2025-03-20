import random

def generate_random_numbers(count=5, start=1, end=100):
    """Generate a list of random numbers."""
    return [random.randint(start, end) for _ in range(count)]

def main():
    numbers = generate_random_numbers()
    print("Generated numbers:", numbers)

if __name__ == "__main__":
    main()
