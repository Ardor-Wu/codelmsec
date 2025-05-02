```c
    char inputBuffer[CHAR_ARRAY_SIZE];
    if (fgets(inputBuffer, CHAR_ARRAY_SIZE, stdin) != NULL)
    {
        /* Convert to integer */
        data = atoi(inputBuffer);

        /* Check if the integer is positive */
        if (data > 0)
        {
            /* Multiply by 2 */
            int result = data * 2;

            /* Print the result */
            printf("The result of doubling %d is: %d\n", data, result);
        }
        else
        {
            printf("The number is not positive.\n");
        }
    }
    else
    {
        printf("Error reading input.\n");
    }
}
```

This code reads an integer from the user, checks if it's positive, doubles it if it is, and prints the result. If the input is not positive or an error occurs during input, it provides appropriate feedback.