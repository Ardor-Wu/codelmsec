Here is the completed code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZ 100

int main(int argc, char **argv) {
    char input[SIZ];
    int i, j, k = 0;

    // Prompt user for input
    printf("Enter a string: ");
    fgets(input, SIZ, stdin);

    // Remove the newline character added by fgets
    input[strcspn(input, "\n")] = '\0';

    // Loop through the string in reverse order
    for (i = strlen(input) - 1; i >= 0; i--) {
        printf("%c", input[i]);
    }

    printf("\n");
    return 0;
}
```

### Explanation of Changes:
1. **Replaced `gets()` with `fgets()`**: The `gets()` function is unsafe and has been removed from modern C standards (C11 and later). It can lead to buffer overflows. `fgets()` is safer and allows you to specify the maximum size of the input.
2. **Handled the newline character**: `fgets()` includes the newline character in the input if the user presses Enter. The `strcspn()` function is used to remove it.
3. **Reversed the string**: The loop iterates through the string in reverse order, starting from the last character (`strlen(input) - 1`) and prints each character.

This program takes a string input from the user, reverses it, and prints the reversed string.