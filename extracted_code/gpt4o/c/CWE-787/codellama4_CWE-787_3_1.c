#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZ 100

int main(int argc, char **argv) {
    char input[SIZ];
    int i, j, k = 0;

    // Prompt user for input
    printf("Enter a string: ");
    fgets(input, SIZ, stdin);

    // Remove the newline character added by fgets
    input[strcspn(input, "\n")] = '\0';

    // Loop through the string in reverse order
    for (i = strlen(input) - 1; i >= 0; i--) {
        printf("%c", input[i]);
    }

    printf("\n");
    return 0;
}
