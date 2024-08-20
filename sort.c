#include <stdio.h>
#include <stdlib.h>

// Function to perform insertion sort
void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        /* Move elements of arr[0..i-1], that are
           greater than key, to one position ahead
           of their current position */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main(int argc, char *argv[]) {
    FILE *file;
    int *numbers = NULL;
    int size = 0;
    int capacity = 10; // Initial capacity for the array
    int num;

    // Check if filename is provided as argument
    if (argc != 2) {
        fprintf(stderr, "Usage: %s filename\n", argv[0]);
        return 1;
    }

    // Open the file
    file = fopen(argv[1], "r");
    if (file == NULL) {
        fprintf(stderr, "Error opening file\n");
        return 1;
    }

    // Allocate memory for the array
    numbers = (int *)malloc(capacity * sizeof(int));
    if (numbers == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Read numbers from the file
    while (fscanf(file, "%d", &num) == 1) {
        // Check if array needs to be resized
        if (size == capacity) {
            capacity *= 2;
            numbers = (int *)realloc(numbers, capacity * sizeof(int));
            if (numbers == NULL) {
                fprintf(stderr, "Memory reallocation failed\n");
                return 1;
            }
        }
        // Store the number in the array
        numbers[size++] = num;
    }

    // Close the file
    fclose(file);

    // Perform insertion sort
    insertionSort(numbers, size);
    
    // Print sorted numbers
    for (int i = 0; i < size; i++) {
        printf("%d\n", numbers[i]);
    }

    // Free dynamically allocated memory
    free(numbers);

    return 0;
}
