#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>

/*
 * Define a union with two members of int and unsigned int type respectively
 */
typedef union myUnion_t {
    int unionFirst;
    unsigned int unionSecond;
} myUnion;

/*
 * The updateAndPrint function reads an integer from stdin, adds it to the
 * second union member and prints the updated value
 */
void updateAndPrint(myUnion *u) {
    int input;
    printf("Enter an integer: ");
    if (scanf("%d", &input) != 1) {
        fprintf(stderr, "Error reading input.\n");
        return;
    }

    // Add the input to the second union member
    u->unionSecond += input;

    // Print the updated value of the second union member
    printf("Updated value of unionSecond: %u\n", u->unionSecond);
}

int main() {
    myUnion u;
    u.unionSecond = 0; // Initialize the second union member to 0

    updateAndPrint(&u);

    return 0;
}
