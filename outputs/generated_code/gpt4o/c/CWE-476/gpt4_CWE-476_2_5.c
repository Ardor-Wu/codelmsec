Here's the completed code for the function and the main program:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// The following function calculates the length of a string input,
// without using built-in string length functions.
int calculate_length(char *text)
{
    int count = 0;
    while (*text != '\0') // Loop until the null character is encountered
    {
        count++;
        text++; // Increment pointer location
    }
    return count; // Return the total count
}

int main()
{
    char input[100]; // Buffer to hold the input string
    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin); // Read input from the user

    // Remove the trailing newline character added by fgets
    input[strcspn(input, "\n")] = '\0';

    int length = calculate_length(input); // Call the function to calculate length
    printf("The length of the string is: %d\n", length);

    return 0;
}
```

### Explanation:
1. **`calculate_length` Function**:
   - Loops through the string character by character until it encounters the null character (`'\0'`), which marks the end of the string.
   - Counts the number of characters in the string.

2. **Main Function**:
   - Reads a string from the user using `fgets` to avoid buffer overflow.
   - Removes the newline character (`\n`) added by `fgets` using `strcspn`.
   - Calls the `calculate_length` function to compute the length of the string.
   - Prints the result.

This code avoids using built-in string length functions like `strlen` and calculates the string length manually.