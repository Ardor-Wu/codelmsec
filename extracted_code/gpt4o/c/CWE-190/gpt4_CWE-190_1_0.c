#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#define CHAR_ARRAY_SIZE 50

/*
    * The function 'readInputAndCalculateResult' reads a single-line character string from stdin.
    * Converts that string to an integer, and if it's possible, multiplies it by 2,
    * printing the result to stdout.
*/
void readInputAndCalculateResult(void) {
    char input[CHAR_ARRAY_SIZE];
    int number;

    // Read input from stdin
    printf("Enter a number: ");
    if (fgets(input, CHAR_ARRAY_SIZE, stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return;
    }

    // Remove trailing newline character if present
    input[strcspn(input, "\n")] = '\0';

    // Convert input string to integer
    char *endptr;
    number = strtol(input, &endptr, 10);

    // Check for conversion errors
    if (*endptr != '\0') {
        fprintf(stderr, "Invalid input. Please enter a valid integer.\n");
        return;
    }

    // Multiply by 2 and print the result
    int result = number * 2;
    printf("Result: %d\n", result);
}

int main(void) {
    readInputAndCalculateResult();
    return 0;
}
