import sys

def main():
    if len(sys.argv) == 3:
        name = sys.argv[1]
        age = int(sys.argv[2])
        print(f"Hello {name}, you are {age} years old.")
    else:
        print(f"Usage: python {sys.argv[0]} [name] [age]")

if __name__ == "__main__":
    main()