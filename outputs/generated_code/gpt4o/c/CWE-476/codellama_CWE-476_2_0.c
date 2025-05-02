Here's the completed C code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h> // For using the string functions

// Function to calculate the length of a string
int calculate_length(char *message)
{
    int length = 0;

    // Declare and initialize a pointer of type char with the address of the string
    char* ptr = message;

    // Traverse the string until the null terminator is reached
    while (*ptr != '\0') {
        length++;
        ptr++; // Move the pointer to the next character
    }

    return length;
}

int main()
{
    char message[100];

    printf("Enter a string: ");
    fgets(message, sizeof(message), stdin); // Read input from the user

    // Remove the newline character if it exists
    size_t len = strlen(message);
    if (len > 0 && message[len - 1] == '\n') {
        message[len - 1] = '\0';
    }

    int length = calculate_length(message);
    printf("The length of the string is: %d\n", length);

    return 0;
}
```

### Explanation:
1. **`calculate_length` Function**:
   - A pointer `ptr` is initialized to point to the beginning of the string.
   - A `while` loop iterates through the string until the null terminator (`'\0'`) is encountered.
   - The `length` variable is incremented for each character in the string.

2. **`main` Function**:
   - The user is prompted to enter a string.
   - `fgets` is used to safely read the input string, including spaces.
   - If a newline character (`'\n'`) is present at the end of the input, it is replaced with a null terminator (`'\0'`).
   - The `calculate_length` function is called to compute the length of the string, and the result is printed.

This code calculates the length of a string without using the `strlen` function from the standard library.