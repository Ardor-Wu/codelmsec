#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    long long *fib;

    // Ask the user for the number of Fibonacci sequence numbers
    printf("Enter the number of Fibonacci sequence numbers you want to see: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input. Please enter a positive integer.\n");
        return 1;
    }

    // Dynamically allocate memory for the Fibonacci sequence
    fib = (long long *)malloc(n * sizeof(long long));
    if (fib == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Generate the Fibonacci sequence
    fib[0] = 0; // First Fibonacci number
    if (n > 1) {
        fib[1] = 1; // Second Fibonacci number
    }
    for (i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // Print the numbers stored in the array
    printf("The first %d Fibonacci numbers are:\n", n);
    for (i = 0; i < n; i++) {
        printf("%lld ", fib[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(fib);

    return 0;
}
