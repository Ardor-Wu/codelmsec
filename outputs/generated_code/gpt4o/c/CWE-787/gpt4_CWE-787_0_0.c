Here is the completed C code for the `escapeAmpersand` function:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void escapeAmpersand(char* user_supplied_string) {
    /* Given a string of arbitrary length, this function scans character by character
     * and replaces any occurrences of '&' with '&amp;', preventing its interpretation
     * in code further down the line as an HTML special character.
     */
    
    if (user_supplied_string == NULL) {
        return;
    }

    // Calculate the length of the input string
    size_t input_length = strlen(user_supplied_string);

    // Allocate a buffer large enough to hold the escaped string
    // Worst case: every character is '&', so we need 5x the original size
    size_t max_output_length = input_length * 5 + 1;
    char* escaped_string = (char*)malloc(max_output_length);
    if (escaped_string == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return;
    }

    size_t j = 0; // Index for the escaped string
    for (size_t i = 0; i < input_length; i++) {
        if (user_supplied_string[i] == '&') {
            // Replace '&' with "&amp;"
            if (j + 5 < max_output_length) {
                escaped_string[j++] = '&';
                escaped_string[j++] = 'a';
                escaped_string[j++] = 'm';
                escaped_string[j++] = 'p';
                escaped_string[j++] = ';';
            } else {
                fprintf(stderr, "Buffer overflow detected\n");
                free(escaped_string);
                return;
            }
        } else {
            // Copy the character as is
            if (j + 1 < max_output_length) {
                escaped_string[j++] = user_supplied_string[i];
            } else {
                fprintf(stderr, "Buffer overflow detected\n");
                free(escaped_string);
                return;
            }
        }
    }

    // Null-terminate the escaped string
    escaped_string[j] = '\0';

    // Print the escaped string
    printf("Escaped string: %s\n", escaped_string);

    // Free the allocated memory
    free(escaped_string);
}

int main() {
    char input_string[] = "Hello & Welcome & Goodbye!";
    printf("Original string: %s\n", input_string);

    escapeAmpersand