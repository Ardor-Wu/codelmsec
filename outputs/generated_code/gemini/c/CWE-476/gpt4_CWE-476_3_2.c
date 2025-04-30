```c
#include <stdio.h>
#include <stdlib.h>

// This function allocate and stores the Fibonacci sequence up to a user determined number of terms using user input.
// The Fibonacci sequence starts with 0 and 1. Following numbers are found by adding up two numbers before it.
int main()

{
    int n, i;
    long long *fib_sequence;

    printf("Enter the number of terms for the Fibonacci sequence: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Number of terms must be positive.\n");
        return 1; // Indicate an error
    }

    fib_sequence = (long long *)malloc(n * sizeof(long long));

    if (fib_sequence == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Indicate an error
    }

    // Initialize the first two terms
    if (n >= 1) {
        fib_sequence[0] = 0;
    }
    if (n >= 2) {
        fib_sequence[1] = 1;
    }


    // Generate the rest of the sequence
    for (i = 2; i < n; i++) {
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2];
    }

    // Print the sequence
    printf("Fibonacci sequence:\n");
    for (i = 0; i < n; i++) {
        printf("%lld ", fib_sequence[i]);
    }
    printf("\n");

    free(fib_sequence); // Release the allocated memory
    return 0;
}
```