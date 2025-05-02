#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>

static const int START_OF_STRING = 0;
static const int END_OF_STRING = -1;

void readAndPrintChar(void)
{
    char data[100];

    /* Read input from stdin */
    if (fgets(data, sizeof(data), stdin) != NULL) {
        /* Print the input string */
        printf("You entered: %s", data);
    } else {
        printf("Error reading input.\n");
    }
}

int main(void)
{
    printf("Enter a string: ");
    readAndPrintChar();
    return 0;
}
