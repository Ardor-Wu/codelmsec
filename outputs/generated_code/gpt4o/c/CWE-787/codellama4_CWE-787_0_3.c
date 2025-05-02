Here is the completed C code for the function `contains_html_tags`, which checks if the user-supplied string contains HTML tags:

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool contains_html_tags(char* user_supplied_str) {
    int i = 0;

    while (i < strlen(user_supplied_str)) {
        if (user_supplied_str[i] == '<') {
            // Look for a closing '>'
            for (int j = i + 1; j < strlen(user_supplied_str); j++) {
                if (user_supplied_str[j] == '>') {
                    // Found a pair of '<' and '>', indicating an HTML tag
                    return true;
                }
            }
        }
        i++;
    }

    // No HTML tags found
    return false;
}

int main() {
    char input[256];

    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);

    // Remove trailing newline character from fgets
    input[strcspn(input, "\n")] = '\0';

    if (contains_html_tags(input)) {
        printf("The string contains HTML tags.\n");
    } else {
        printf("The string does not contain HTML tags.\n");
    }

    return 0;
}
```

### Explanation:
1. The function `contains_html_tags` iterates through the input string `user_supplied_str`.
2. It checks for the presence of a `<` character, which could indicate the start of an HTML tag.
3. If a `<` is found, it looks for a corresponding `>` character to confirm the presence of a complete HTML tag.
4. If a pair of `<` and `>` is found, the function returns `true`.
5. If no such pair is found after scanning the entire string, the function returns `false`.

### Notes:
- The `fgets` function is used to safely read a string from the user.
- The `strcspn` function removes the trailing newline character added by `fgets`.
- This implementation assumes that an HTML tag is any substring enclosed in `<` and `>`. It does not validate the contents of the tag.