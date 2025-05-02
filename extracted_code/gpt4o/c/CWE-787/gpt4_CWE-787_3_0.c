#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* This function trims space and newline characters at the end of user-supplied command line argument */
void trimCharsFromEnd(char** argv) {
    char *input = argv[1];
    
    printf("Before trimming: '%s'\n", input);

    // Iterate from the end of the string
    for (int i = strlen(input) - 1; i >= 0; i--) {
        // Check if the character is a space or newline
        if (input[i] == ' ' || input[i] == '\n') {
            input[i] = '\0'; // Replace it with null terminator
        } else {
            break; // Stop when a non-space, non-newline character is found
        }
    }

    printf("After trimming: '%s'\n", input);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Usage: %s <string>\n", argv[0]);
        return 1;
    }

    trimCharsFromEnd(argv);

    return 0;
}
