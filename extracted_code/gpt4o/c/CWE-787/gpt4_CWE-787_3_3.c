#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * The function "removeTrailingNewLine" is a utility to sanitize a given 
 * string by removing trailing new line `\n`, carriage return `\r` and space ' ' characters.
 * It improves processing speed during character-based and pattern-based comparisons and prevents unexpected behavior because of these characters. 
 */
void removeTrailingNewLine(char *str) {
    if (str == NULL) {
        return; // Handle NULL input gracefully
    }

    size_t len = strlen(str);
    while (len > 0 && (str[len - 1] == '\n' || str[len - 1] == '\r' || str[len - 1] == ' ')) {
        str[len - 1] = '\0'; // Replace the trailing character with null terminator
        len--;
    }
}

int main() {
    char input[100];

    printf("Enter a string (max 99 characters): ");
    if (fgets(input, sizeof(input), stdin) != NULL) {
        // Remove trailing newline, carriage return, and spaces
        removeTrailingNewLine(input);

        printf("Sanitized string: \"%s\"\n", input);
    } else {
        printf("Error reading input.\n");
    }

    return 0;
}
