#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>

#define CHAR_ARRAY_SIZE 50

/* Function prototype */
void inputForPrinting();

int main() {
    inputForPrinting();
    return 0;
}

void inputForPrinting() {
    char inputBuffer[CHAR_ARRAY_SIZE];
    int number;

    printf("Enter a positive integer: ");
    
    /* Read input from the user */
    if (fgets(inputBuffer, CHAR_ARRAY_SIZE, stdin) != NULL) {
        /* Remove newline character if present */
        size_t len = strlen(inputBuffer);
        if (len > 0 && inputBuffer[len - 1] == '\n') {
            inputBuffer[len - 1] = '\0';
        }

        /* Convert input string to integer */
        number = atoi(inputBuffer);

        /* Check if the number is positive */
        if (number > 0) {
            /* Double the number and print the result */
            int doubledValue = number * 2;
            printf("The doubled value is: %d\n", doubledValue);
        } else {
            printf("The input is not a positive integer.\n");
        }
    } else {
        printf("Error reading input.\n");
    }
}
