(char *)malloc(100 * sizeof(char)); // Allocate memory for the message

    if (message == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Exit if memory allocation fails
    }

    printf("Enter a string: ");
    fgets(message, 100, stdin); // Read input from the user

    // Remove the newline character if present
    size_t len = strlen(message);
    if (len > 0 && message[len - 1] == '\n') {
        message[len - 1] = '\0';
    }

    int length = calculate_length(message); // Call the function to calculate length
    printf("The length of the string is: %d\n", length);

    free(message); // Free the allocated memory
    return 0;
}
