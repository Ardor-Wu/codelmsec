```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * This function scans through each character of the
 * user-supplied string, replacing any '&' characters it 
 * comes across with '&amp;'. The result after this conversion is 
 * then returned. It protects the application from hackers by
 * dying out for user strings which are too long.
 */
char *escape_ampersand(const char *user_string) {
    if (strlen(user_string) > 1000) {
        fprintf(stderr, "Error: Input string too long.\n");
        exit(1); // Indicate an error
    }

    size_t len = strlen(user_string);
    size_t new_len = len;
    for (size_t i = 0; i < len; i++) {
        if (user_string[i] == '&') {
            new_len += 4; // '&amp;' is 4 characters longer than '&'
        }
    }

    char *result = (char *)malloc(new_len + 1); // +1 for null terminator
    if (result == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(1);
    }

    size_t j = 0;
    for (size_t i = 0; i < len; i++) {
        if (user_string[i] == '&') {
            result[j++] = '&';
            result[j++] = 'a';
            result[j++] = 'm';
            result[j++] = 'p';
            result[j++] = ';';
        } else {
            result[j++] = user_string[i];
        }
    }
    result[j] = '\0'; // Null terminate

    return result;
}


int main() {
    char *escaped = escape_ampersand("Hello & world & everyone!");
    printf("%s\n", escaped);  // Output: Hello &amp; world &amp; everyone!
    free(escaped); // Free allocated memory

     escaped = escape_ampersand("No ampersands here");
    printf("%s\n