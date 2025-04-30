```c
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
    int remainder, i = 1, step = 1;

    while (num != 0)
    {
        remainder = num % 16;
        hexa += remainder * i;
        i *= 10;
        num /= 16;
    }
    return hexa;
}

int main(void)
{
    printf("%u\n", STATIC_CONST_FIVE);
    return 0;

}
```