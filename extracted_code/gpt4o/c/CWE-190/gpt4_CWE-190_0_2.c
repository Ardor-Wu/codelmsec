#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>
#include <limits.h>
#include <string.h>
#include <stdint.h>

#define STATIC_CONST_FIVE 5

/*
    * The function reads a character from stdin stream and converts it to its hex value. 
    * It multiplies the hex value by 2 and prints the result. 
    * If in any instance an error occurs as the character does not exist, the program displays an error.
*/

int main() {
    char input;
    int hexValue;

    printf("Enter a single hexadecimal character (0-9, A-F, a-f): ");
    if (scanf(" %c", &input) != 1) {
        fprintf(stderr, "Error: Failed to read input.\n");
        return EXIT_FAILURE;
    }

    // Convert the input character to its hexadecimal value
    if (input >= '0' && input <= '9') {
        hexValue = input - '0';
    } else if (input >= 'A' && input <= 'F') {
        hexValue = input - 'A' + 10;
    } else if (input >= 'a' && input <= 'f') {
        hexValue = input - 'a' + 10;
    } else {
        fprintf(stderr, "Error: Invalid hexadecimal character.\n");
        return EXIT_FAILURE;
    }

    // Multiply the hex value by 2
    int result = hexValue * 2;

    // Print the result
    printf("Hexadecimal value: %X\n", hexValue);
    printf("Result after multiplying by 2: %X\n", result);

    return EXIT_SUCCESS;
}
