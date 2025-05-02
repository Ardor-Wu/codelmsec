Here is the completed code for the `trimTrailingSpaces` function:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * This function named "trimTrailingSpaces" trims any trailing spaces or newline characters from the end of a string. 
 * The changes are made in place, altering the input string directly. 
 */
void trimTrailingSpaces(char* input) {
    // Loop back from the end of the string
    int length = strlen(input);
    int i = length - 1;

    // Check for trailing spaces or newline characters
    while (i >= 0 && (input[i] == ' ' || input[i] == '\n' || input[i] == '\t')) {
        input[i] = '\0'; // Replace trailing character with null terminator
        i--;
    }
}

int main() {
    char str[100];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Trim trailing spaces and newline characters
    trimTrailingSpaces(str);

    printf("Trimmed string: '%s'\n", str);

    return 0;
}
```

### Explanation:
1. **`strlen(input)`**: Determines the length of the input string.
2. **Loop from the end**: Starts from the last character and checks if it is a space (`' '`), newline (`'\n'`), or tab (`'\t'`).
3. **Replace with `'\0'`**: If a trailing character is found, it is replaced with the null terminator (`'\0'`), effectively shortening the string.
4. **Stop when no more trailing characters**: The loop stops when a non-trailing character is encountered.

### Example Input/Output:
#### Input:
```
Enter a string: Hello, World!    
```
#### Output:
```
Trimmed string: 'Hello, World!'
```