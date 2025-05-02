#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>

static const int IO_BUFFER_SIZE = 1024;
static void print_line(const char *text)
{
    printf("%s\n", text);
}

#define CHARS_IN_UINT32 10 /* 2^32 can have a maximum of 10 decimal digits */

static void uint32_to_string(uint32_t value, char *buffer, size_t buffer_size)
{
    if (buffer_size < CHARS_IN_UINT32 + 1) // +1 for null terminator
    {
        print_line("Buffer size is too small to hold the uint32 string.");
        return;
    }

    snprintf(buffer, buffer_size, "%u", value);
}

int main()
{
    uint32_t number = 4294967295; // Maximum value for uint32_t
    char buffer[CHARS_IN_UINT32 + 1]; // +1 for null terminator

    uint32_to_string(number, buffer, sizeof(buffer));
    print_line("The uint32 number as a string is:");
    print_line(buffer);

    return 0;
}
