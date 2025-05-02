#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h> // Include string.h for memset

static const int IO_BUFFER_SIZE = 1024;

void printLine(char *data)
{
    char* buffer = (char*)malloc(sizeof(char) * IO_BUFFER_SIZE);
    if (buffer == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return;
    }

    memset(buffer, '\0', IO_BUFFER_SIZE); // Initialize buffer with null characters
    strncpy(buffer, data, IO_BUFFER_SIZE - 1); // Copy data into buffer, ensuring no overflow
    printf("%s\n", buffer); // Print the buffer content
    free(buffer); // Free allocated memory
}

int main()
{
    char input[] = "Hello, World!";
    printLine(input);
    return 0;
}
