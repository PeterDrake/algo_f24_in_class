import sys


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def main():
    if len(sys.argv) != 2:
        print("Usage: python program_name.py input_file")
        return
    file_name = sys.argv[1]
    try:
        with open(file_name, "r") as file:
            numbers = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print("File not found.")
        return
    sorted_numbers = quicksort(numbers)
    for num in sorted_numbers:
        print(num)


if __name__ == "__main__":
    main()
