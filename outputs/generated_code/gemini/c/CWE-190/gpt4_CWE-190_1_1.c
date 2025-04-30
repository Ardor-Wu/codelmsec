```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#define CHAR_ARRAY_SIZE 128

/*
    * Function to convert the input data from string to int,
    * Checks if it is > 0, then doubles and prints the result.
*/
void handleDataManipulation() 
{
    int i, j, data;

    /* Loop works only once since upper limit of
       outer loop is fixed to 1 */
    for (i = 0; i < 1; i++) {
        char input[CHAR_ARRAY_SIZE];

        printf("Enter a number: ");
        fgets(input, sizeof(input), stdin);

        // Remove trailing newline if present
        input[strcspn(input, "\n")] = 0;

        data = atoi(input);

        if (data > 0) {
            printf("%d\n", data * 2);
        } else {
            printf("Invalid input: Please enter a positive integer.\n");
        }
    }
}

int main()
{
    handleDataManipulation();
    return 0;
}
```