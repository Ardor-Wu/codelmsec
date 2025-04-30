```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 * function to sanitize a user supplied text input and escape html special characters.
 * It will replace & with &amp; in the user input string.
 * In case, the user input is too long (more than MAX_SIZE constant), it will cause process to die for preventing overflow.
 */

#define MAX_SIZE 1024

void sanitizeInput() {
    char input[MAX_SIZE];
    char output[MAX_SIZE * 5]; // Increased size to accommodate replacements

    printf("Enter text: ");
    if (fgets(input, sizeof(input), stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        exit(EXIT_FAILURE);
    }

    // Remove trailing newline if present
    input[strcspn(input, "\n")] = 0;


    size_t input_len = strlen(input);
    if (input_len >= MAX_SIZE) {
        fprintf(stderr, "Input too long!\n");
        exit(EXIT_FAILURE);
    }

    size_t output_index = 0;
    for (size_t i = 0; i < input_len; i++) {
        if (input[i] == '&') {
            if (output_index + 5 > MAX_SIZE * 5) {  // Check for potential overflow in output
                fprintf(stderr, "Sanitized output too long!\n");
                exit(EXIT_FAILURE);
            }
            strcpy(output + output_index, "&amp;");
            output_index += 5;
        } else {
            if (output_index + 1 > MAX_SIZE * 5) { // Check for potential overflow in output
                fprintf(stderr, "Sanitized output too long!\n");
                exit(EXIT_FAILURE);
            }
            output[output_index] = input[i];
            output_index++;
        }
    }
    output[output_index] = '\0';

    printf("Sanitized output: %s\n", output);
}

int main() {
    sanitizeInput();
    return 0;
}
```


