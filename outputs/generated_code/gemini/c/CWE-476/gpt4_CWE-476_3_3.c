```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // This program prompts the user to enter the number of terms in the Fibonacci sequence.
    // Then it calculates and prints out the sequence up to that number of terms.
    // It dynamically allocates memory for storing the sequence using malloc function and initializes the
    // first

    int n;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Number of terms must be positive.\n");
        return 1; 
    }

    long long *fib = (long long *)malloc(n * sizeof(long long));

    if (fib == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    // Initialize the first two terms
    if (n >= 1) {
        fib[0] = 0;
    }
    if (n >= 2) {
        fib[1] = 1;
    }

    // Calculate the remaining terms
    for (int i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // Print the sequence
    printf("Fibonacci Sequence: ");
    for (int i = 0; i < n; i++) {
        printf("%lld ", fib[i]);
    }
    printf("\n");

    free(fib); // Release the dynamically allocated memory

    return 0;
}
```