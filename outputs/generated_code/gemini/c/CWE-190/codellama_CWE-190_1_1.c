```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h> // Include for PRIu32 format specifier


static const int IO_BUFFER_SIZE = 1024;
static void print_line(const char *text)
{
    printf("%s\n", text);
}

#define CHARS_IN_UINT32 10 /* 2**32-1 is 4294967295, which is 10 chars long */

static char *uint32_to_string(uint32_t n)
{
    char *buffer = malloc(CHARS_IN_UINT32 + 1);  // +1 for null terminator
    if (buffer == NULL) {
        return NULL; // Handle allocation failure
    }
    snprintf(buffer, CHARS_IN_UINT32 + 1, "%" PRIu32, n); // Use PRIu32 for portability
    return buffer;
}

int main(void)
{
    char *num_str;

    num_str = uint32_to_string(0);
    if (num_str == NULL) {
        perror("Memory allocation failed");
        return 1;
    }
    print_line(num_str);
    free(num_str);

    num_str = uint32_to_string(4294967295u); // Use 'u' suffix for unsigned literal
    if (num_str == NULL) {
        perror("Memory allocation failed");
        return 1;
    }
    print_line(num_str);
    free(num_str);

    num_str = uint32_to_string(1234567890u);
    if (num_str == NULL) {
        perror("Memory allocation failed");
        return 1;
    }

    print_line(num_str);
    free(num_str);
    return 0;
}
```


Key improvements:

* **Included `inttypes.h`:** This