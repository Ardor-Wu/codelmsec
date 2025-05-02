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
