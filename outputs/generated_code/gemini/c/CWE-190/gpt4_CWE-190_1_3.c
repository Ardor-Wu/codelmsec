```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#include <limits.h> // For INT_MAX and INT_MIN
#include <errno.h>  // For errno

#define CHAR_ARRAY_SIZE 50

/* 
    * The function collects inputs, convert the input string to integer and doubles it.
    inputForPrinting() function performs reading of data in the CHAR_ARRAY_SIZE buffer size.
    Converts the read data into int, checks whether it's positivity.
    If so, it will double
*/
void inputForPrinting() {
    char input[CHAR_ARRAY_SIZE];
    long num;
    char *endptr;

    printf("Enter a number: ");
    if (fgets(input, sizeof(input), stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return;
    }

    // Remove trailing newline if present
    input[strcspn(input, "\n")] = 0;

    errno = 0; // Clear errno before calling strtol
    num = strtol(input, &endptr, 10);

    // Error checking for strtol
    if (errno == ERANGE) {
        if (num == LONG_MAX) {
            fprintf(stderr, "Input number is too large.\n");
        } else if (num == LONG_MIN) {
            fprintf(stderr, "Input number is too small.\n");
        }
        return;

    } else if (endptr == input || *endptr != '\0') {  // Check for invalid characters
        fprintf(stderr, "Invalid input: Not a valid integer.\n");
        return;
    }


    if (num > 0) {
        if (num > INT_MAX / 2) {  // Check for potential overflow after doubling
            fprintf(stderr, "Doubling the number would cause overflow.\n");
        } else {
             printf("Doubled value: %ld\n", num * 2);
        }
       
    } else {
        printf("The number is not positive.\n");
    }
}