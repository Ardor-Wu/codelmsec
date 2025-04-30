```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // The function prompts the user to enter the 
    // number of terms in the Fibonacci sequence then it prints the sequence.
    int *fib = NULL;
    // Declare an integer variable
    int n;

    printf("Enter the number of terms in the Fibonacci sequence: ");
    scanf("%d", &n);

    // Validate the input
    if (n <= 0) {
        printf("Please enter a positive integer.\n");
        return 1; // Indicate an error
    }

    // Allocate memory dynamically for the Fibonacci sequence
    fib = (int *)malloc(n * sizeof(int));

    // Check if memory allocation was successful
    if (fib == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Indicate an error
    }

    // Generate the Fibonacci sequence
    if (n >= 1) {
        fib[0] = 0;
    }
    if (n >= 2) {
        fib[1] = 1;
    }
    for (int i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    // Print the Fibonacci sequence
    printf("Fibonacci sequence: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", fib[i]);
    }
    printf("\n");

    // Free the dynamically allocated memory
    free(fib);

    return 0;
}
```