```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void escapeAmpersand(char* user_supplied_string) {
    /* Given a string of arbitrary length, this function scans character by character
    * and replaces any occurrences of '&' with '&amp;', preventing its interpretation
    * in code further down the line as html special character. 
    * Also
    */
    if (user_supplied_string == NULL) {
        return; // Handle NULL input
    }

    size_t len = strlen(user_supplied_string);
    size_t new_len = len;
    for (size_t i = 0; i < len; i++) {
        if (user_supplied_string[i] == '&') {
            new_len += 4; // '&amp;' is 4 chars longer than '&'
        }
    }


    if (new_len == len) {
        return; // No '&' found, nothing to do.
    }

    char* new_string = (char*)malloc((new_len + 1) * sizeof(char)); // +1 for null terminator
    if (new_string == NULL) {
        // Handle memory allocation failure
        perror("Memory allocation failed");
        return; 
    }

    size_t j = 0;
    for (size_t i = 0; i < len; i++) {
        if (user_supplied_string[i] == '&') {
            new_string[j++] = '&';
            new_string[j++] = 'a';
            new_string[j++] = 'm';
            new_string[j++] = 'p';
            new_string[j++] = ';';
        } else {
            new_string[j++] = user_supplied_string[i];
        }
    }
    new_string[j] = '\0';

    strcpy(user_supplied_string, new_string); // Copy the escaped string back
    free(new_string); // Free the allocated memory

}



int main() {
    char test_string[100] = "This string contains an ampersand & and another one &.";
