# main.py
from utils import add_numbers, multiply_numbers

if __name__ == "__main__":
    print("Hello from main.py!")
    result_add = add_numbers(5, 3)
    result_multiply = multiply_numbers(5, 3)
    print(f"Add result: {result_add}")
    print(f"Multiplн result: {result_multiply}")
