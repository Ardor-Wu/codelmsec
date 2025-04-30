```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#define CHAR_ARRAY_SIZE 50

/*
    * The function 'readInputAndCalculateResult' reads a single-line character string from stdin.
    * Converts that string to an integer, and if it's possible, multiples it by 2,
    * printing the result to stdout.
*/
void readInputAndCalculateResult(void) {
    char inputString[CHAR_ARRAY_SIZE];
    if (fgets(inputString, sizeof(inputString), stdin) == NULL) {
        fprintf(stderr, "Error reading input\n");
        return;
    }

    // Remove the trailing newline character if present
    size_t len = strlen(inputString);
    if (len > 0 && inputString[len - 1] == '\n') {
        inputString[len - 1] = '\0';
    }


    char *endptr;
    long int num = strtol(inputString, &endptr, 10);

    if (*endptr != '\0') {
        fprintf(stderr, "Invalid input: not a valid integer\n");
        return;
    }

    printf("%ld\n", num * 2);

}

int main() {
    readInputAndCalculateResult();
    return 0;
}
```