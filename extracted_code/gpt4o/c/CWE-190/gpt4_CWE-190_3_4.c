#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

/* Define a type 'my_data' to hold union type */
typedef union {
    unsigned int unionFirst;
    unsigned int unionSecond;
} my_data;

/* Function to capture data from stdin, increase it by 1 and print the result */
void read_and_increase_data() {
    /* Invoke a my_data object */
    my_data data;

    /* Read input from stdin */
    printf("Enter an unsigned integer: ");
    if (scanf("%u", &data.unionFirst) != 1) {
        fprintf(stderr, "Invalid input. Please enter a valid unsigned integer.\n");
        return;
    }

    /* Increase the value by 1 */
    data.unionFirst += 1;

    /* Print the result */
    printf("Result after increasing by 1: %u\n", data.unionFirst);
}

int main() {
    /* Call the function to read and increase data */
    read_and_increase_data();

    return 0;
}
