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
    int i = strlen(input) - 1;

    // Iterate backwards until a non-space/newline character is found or the beginning of the string is reached.
    while (i >= 0 && (input[i] == ' ' || input[i] == '\n' || input[i] == '\t' || input[i] == '\r')) {
        i--;
    }

    // Null-terminate the string after the last non-space/newline character.
    input[i + 1] = '\0';
}
```