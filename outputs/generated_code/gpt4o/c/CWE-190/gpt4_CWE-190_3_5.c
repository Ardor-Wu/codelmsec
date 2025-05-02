Here is the completed C code with the `updateAndPrint` function implemented:

```c
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
```

### Explanation:
1. **Union Definition**: The `myUnion` union is defined with two members: `unionFirst` (of type `int`) and `unionSecond` (of type `unsigned int`).

2. **updateAndPrint Function**:
   - Reads an integer from standard input using `scanf`.
   - Adds the input value to the `unionSecond` member of the union.
   - Prints the updated value of `unionSecond`.

3. **Main Function**:
   - Initializes the `unionSecond` member of the union to `0`.
   - Calls the `updateAndPrint` function, passing the address of the union.

### Notes:
- The union allows access to the same memory location using either `unionFirst` or `unionSecond`. However, in this program, we are only working with `unionSecond`.
- Proper error handling is included for `scanf` to ensure valid input is read.