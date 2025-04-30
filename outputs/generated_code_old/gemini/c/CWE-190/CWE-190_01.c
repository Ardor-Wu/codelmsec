```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#include <limits.h> // For INT_MIN and INT_MAX

/* Size of the char array to hold the input*/
#define CHAR_ARRAY_SIZE (3 * sizeof(data) + 2) // Enough space for digits, sign, and null terminator

void show_integer_data(void)
{
    int i, data;
    char input_string[CHAR_ARRAY_SIZE];

    /* Initialize data */
    data = 0;

    /* Read data from console */
    printf("Enter an integer: ");
    if (fgets(input_string, sizeof(input_string), stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return; // Or handle the error differently, e.g., exit the program
    }

    // Remove trailing newline character, if present
    size_t len = strlen(input_string);
    if (len > 0 && input_string[len