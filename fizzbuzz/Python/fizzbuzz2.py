"""FizzBuzz Coding Kata"""

from fizzbuzz_rules import fizzbuzz2


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz2(num))
