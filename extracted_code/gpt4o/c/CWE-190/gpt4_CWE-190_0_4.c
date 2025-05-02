void read_char_print_hexData(void)
{
    char data;
    /* Prompt the user for input */
    printf("Enter a character: ");
    
    /* Read a single character from input */
    if (scanf(" %c", &data) != 1)
    {
        printf("Error reading input.\n");
        return;
    }

    /* Convert the character to its hexadecimal representation and print it */
    printf("Hexadecimal representation of '%c': 0x%X\n", data, (unsigned char)data);

    /* If the data value is greater than zero, multiply it by two and print the result */
    if (data > 0)
    {
        int result = data * 2;

        /* Ensure the multiplication does not overflow */
        if (result > CHAR_MAX)
        {
            printf("Multiplication result exceeds CHAR_MAX. Overflow detected.\n");
        }
        else
        {
            printf("Result after multiplying by 2: %d (0x%X)\n", result, result);
        }
    }
    else
    {
        printf("Data value is not greater than zero. No multiplication performed.\n");
    }
}
