```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h> // Include for PRId64 macro


// Function to print int64_t values
void printInt64Values()
{
    int64_t val1 = 9223372036854775807LL; // Maximum positive value
    int64_t val2 = -9223372036854775807LL - 1LL; // Minimum negative value
    int64_t val3 = 123456789012345LL;
    int64_t val4 = -123456789012345LL;

    // Use PRId64 macro for portability
    printf("Value 1: %" PRId64 "\n", val1);
    printf("Value 2: %" PRId6