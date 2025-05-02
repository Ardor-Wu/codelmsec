```c
    int *ptr = NULL;

    // Declare a variable to hold the value to search for
    int valueToCheck;

    // Prompt the user to enter the value to search for
    printf("Enter an integer value to check: ");
    scanf("%d", &valueToCheck);

    // Iterate through the array using a pointer
    ptr = arr; // Point to the start of the array
    int found = 0; // Flag to indicate if the value is found

    for (int i = 0; i < 5; i++) {
        if (*ptr == valueToCheck) {
            found = 1;
            break;
        }
        ptr++; // Move the pointer to the next element
    }

    // Print the result
    if (found) {
        printf("Value %d is in the array.\n", valueToCheck);
    } else {
        printf("Value %d is not in the array.\n", valueToCheck);
    }
}

int main() {
    // Call the function to check if an integer value is in the array
    intElementInArrayCheck();
    return 0;
}
```