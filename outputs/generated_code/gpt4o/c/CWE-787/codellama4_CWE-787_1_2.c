```c
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }

    // Initialize the buffer with some data
    for (int i = 0; i < size; i++) {
        buffer[i] = 'A' + (i % 26); // Fill with letters A-Z cyclically
    }
    buffer[size] = '\0'; // Null-terminate the string

    // Print the buffer
    printf("Buffer contents: %s\n", buffer);

    // Free the allocated memory
    free(buffer);

    return EXIT_SUCCESS;
}
```