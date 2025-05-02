#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    // Prompt the user for the number of terms
    printf("Enter the number of terms in the Fibonacci sequence: ");
    scanf("%d", &n);

    // Check if the input is valid
    if (n <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    // Dynamically allocate memory to store the Fibonacci sequence
    int *fib = (int *)malloc(n * sizeof(int));
    if (fib == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Initialize the first two terms of the Fibonacci sequence
    fib[0] = 0;
    if (n > 1) {
        fib[1] = 1;
    }

    // Calculate the Fibonacci sequence
    for (int i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // Print the Fibonacci sequence
    printf("Fibonacci sequence up to %d terms:\n", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fib[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(fib);

    return 0;
}
