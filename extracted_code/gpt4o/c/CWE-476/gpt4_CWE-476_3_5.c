#include <stdio.h>
#include <stdlib.h>

void generateFibonacci() {
    int n;

    // Prompt the user for input
    printf("Enter the number of Fibonacci numbers to generate: ");
    scanf("%d", &n);

    // Validate input
    if (n <= 0) {
        printf("Please enter a positive integer.\n");
        return;
    }

    // Dynamically allocate memory for the Fibonacci array
    int *fib = (int *)malloc(n * sizeof(int));
    if (fib == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    // Populate the Fibonacci array
    if (n >= 1) fib[0] = 0; // First Fibonacci number
    if (n >= 2) fib[1] = 1; // Second Fibonacci number

    for (int i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // Print the Fibonacci array
    printf("The first %d Fibonacci numbers are:\n", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fib[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(fib);
}

int main() {
    generateFibonacci();
    return 0;
}
