#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>
#include <limits.h>
#include <string.h>
#include <stdint.h>

#define STATIC_CONST_FIVE (int_to_hex(5))

/*
 * Function that converts an integer to hexadecimal
 */
unsigned int int_to_hex(int num)
{
    unsigned int hexa = 0;
    int remainder, i = 1;

    while (num != 0)
    {
        remainder = num % 16; // Get the remainder when dividing by 16
        hexa += remainder * i; // Add the remainder to the hexadecimal value
        num /= 16; // Reduce the number by dividing by 16
        i *= 10; // Move to the next position in the hexadecimal representation
    }

    return hexa;
}

int main()
{
    int num = 5;
    unsigned int hex_value = int_to_hex(num);

    printf("The hexadecimal representation of %d is: %u\n", num, hex_value);

    // Using the STATIC_CONST_FIVE macro
    printf("STATIC_CONST_FIVE evaluates to: %u\n", STATIC_CONST_FIVE);

    return 0;
}
