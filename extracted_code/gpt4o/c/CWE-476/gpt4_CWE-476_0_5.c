printf(": ");
    scanf("%d", &n);

    // Check if the input is valid
    if (n <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    // Dynamically allocate memory for the Fibonacci sequence
    fib = (int *)malloc(n * sizeof(int));
    if (fib == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Generate the Fibonacci sequence
    fib[0] = 0; // First term
    if (n > 1) {
        fib[1] = 1; // Second term
        for (int i = 2; i < n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
    }

    // Print the Fibonacci sequence
    printf("Fibonacci sequence:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", fib[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(fib);

    return 0;
}
