```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void remove_char(char *str, char ch) {
    char *src, *dst;
    for (src = dst = str; *src != '\0'; src++) {
        *dst = *src;
        if (*src != ch) {
            dst++;
        }
    }
    *dst = '\0'; // Null-terminate the modified string
}

int main() {
    char str[100];
    char ch;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0'; // Remove the newline character from input

    printf("Enter the character to remove: ");
    scanf(" %c", &ch);

    remove_char(str, ch);

    printf("Modified string: %s\n", str);

    return 0;
}
```

### Explanation:
1. **`remove_char` function**:
   - Iterates through the string using two pointers: `src` (source) and `dst` (destination).
   - Copies characters from `src` to `dst` only if the character is not equal to `ch`.
   - At the end, null-terminates the modified string.

2. **`main` function**:
   - Reads a string and a character from the user.
   - Calls `remove_char` to remove all occurrences of the specified character from the string.
   - Prints the modified string.

### Example Input/Output:
```
Enter a string: hello world
Enter the character to remove: l
Modified string: heo word
```