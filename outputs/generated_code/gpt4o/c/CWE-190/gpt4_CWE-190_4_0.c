```c
        * 255).
    */
    unsigned char input_char;

    /*
        * Read a character from standard input.
        */
    printf("Enter a character: ");
    input_char = getchar();

    /*
        * Multiply the character's ASCII value by 2.
        */
    unsigned int result = input_char * 2;

    /*
        * Print the result in hexadecimal format.
        */
    printf("Result in hexadecimal: %X\n", result);
}

int main(void)
{
    /*
        * Seed the random number generator (not used in this example, but included for completeness).
        */
    srand((unsigned)time(NULL));

    /*
        * Call the function to demonstrate its functionality.
        */
    convertido_en_hex();

    return 0;
}
```