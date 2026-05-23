import sys
import json


def main():
    if len(sys.argv) == 3:
        array = json.loads(sys.argv[1])
        target = int(sys.argv[2])
        array_length = len(array)
        for i in range(array_length):
            for j in range(i + 1, array_length):
                if array[i] + array[j] == target:
                    print([i, j])
                    return
        print("Not Found")
    else:
        print(f"Correct usage: python {sys.argv[0]} [array] [target]")


if __name__ == "__main__":
    main()
