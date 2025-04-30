```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#include <limits.h> // For INT_MAX and INT_MIN


/* This function reads a string from stdin, converts it to binary format. */

void printBinary() {
    char inputString[100];
    int number;
    int success = 0; // Flag to track successful conversion


    printf("Enter a string (representing an integer): ");
    if (fgets(inputString, sizeof(inputString), stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return;
    }

    // Remove the trailing newline character from fgets
    inputString[strcspn(inputString, "\n")] = 0;


    // Use strtol for more robust integer conversion with error checking
    char *endptr;
    long int longNum = strtol(inputString, &endptr, 10);  // Base 10

    // Check for conversion errors
    if (*endptr !=