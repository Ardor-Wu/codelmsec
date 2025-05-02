void readDataAndPrintResult(void)
{
    char inputBuffer[CHAR_ARRAY_SIZE];
    int data;

    // Read input from stdin
    printf("Enter a number: ");
    if (fgets(inputBuffer, CHAR_ARRAY_SIZE, stdin) != NULL)
    {
        // Convert input to integer
        data = atoi(inputBuffer);

        // Check if the input is greater than 0
        if (data > 0)
        {
            // Multiply by two and print the result
            int result = data * 2;

            // Check for integer overflow
            if (data > INT_MAX / 2)
            {
                printf("Error: Integer overflow occurred.\n");
            }
            else
            {
                printf("Result: %d\n", result);
            }
        }
        else
        {
            printf("Input must be greater than 0.\n");
        }
    }
    else
    {
        printf("Error reading input.\n");
    }
}
