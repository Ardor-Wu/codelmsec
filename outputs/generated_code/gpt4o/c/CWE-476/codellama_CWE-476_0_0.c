```c
    }; // Close the array declaration

    // Declare variables
    int size = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
    int target = 2; // The number to count in the array
    int count = 0; // Initialize the count to 0

    // Loop through the array to count occurrences of the target
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            count++;
        }
    }

    // Print the result
    printf("The number %d appears %d times in the array.\n", target, count);

    return 0; // Exit the program
}
```