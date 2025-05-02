Here is the completed code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to calculate the length of the string
int calculate_length(char *str) {
    int i = 0;
    // While str is not NULL, we keep on traversing 
    while (str[i] != '\0') {
        i++;
    }
    return i; // Return the length of the string
}

int main() {
    char str[100];
    
    // Prompt the user to enter a string
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remove the newline character added by fgets
    str[strcspn(str, "\n")] = '\0';
    
    // Calculate the length of the string
    int length = calculate_length(str);
    
    // Print the length of the string
    printf("The length of the string is: %d\n", length);
    
    return 0;
}
```

### Explanation:
1. **`calculate_length` Function**:
   - Loops through the string until the null terminator (`'\0'`) is encountered.
   - Counts the number of characters in the string.

2. **`main` Function**:
   - Reads a string from the user using `fgets` to avoid buffer overflow.
   - Removes the newline character added by `fgets` using `strcspn`.
   - Calls `calculate_length` to compute the string length.
   - Prints the result.

This program is safe and handles user input properly.