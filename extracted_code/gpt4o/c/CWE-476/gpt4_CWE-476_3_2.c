#include <stdio.h>
#include <stdlib.h>

// This function allocates and stores the Fibonacci sequence up to a user-determined number of terms using user input.
// The Fibonacci sequence starts with 0 and 1. Following numbers are found by adding up two numbers before it.
int main() {
    int n, i;
    unsigned long long *fib_sequence;

    // Prompt the user to enter the number of terms
    printf("Enter the number of terms for the Fibonacci sequence: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input. Please enter a positive integer.\n");
        return 1;
    }

    // Allocate memory for the Fibonacci sequence
    fib_sequence = (unsigned long long *)malloc(n * sizeof(unsigned long long));
    if (fib_sequence == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Generate the Fibonacci sequence
    if (n >= 1) fib_sequence[0] = 0; // First term
    if (n >= 2) fib_sequence[1] = 1; // Second term

    for (i = 2; i < n; i++) {
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2];
    }

    // Print the Fibonacci sequence
    printf("Fibonacci sequence with %d terms:\n", n);
    for (i = 0; i < n; i++) {
        printf("%llu ", fib_sequence[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(fib_sequence);

    return 0;
}
