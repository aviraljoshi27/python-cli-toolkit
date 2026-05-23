import sys
from cli_toolkit.utils import number_utils as nu


def main():
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
        even_odd = nu.is_even_or_odd(num)
        print(f"Given number {num} is {even_odd}")
        factorial = nu.factorial(num)
        print(f"Factorial of the given number {num} is {factorial}")
    else:
        print(f"correct usage: python {sys.argv[0]} [num]")


if __name__ == "__main__":
    main()
