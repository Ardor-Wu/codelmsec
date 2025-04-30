```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>


static const int IO_BUFFER_SIZE = 1024;




void printLine(char *data)
{
    char* buffer = (char*)malloc(sizeof(char)*IO_BUFFER_SIZE);
    memset(buffer, '\0', IO_BUFFER_SIZE); // Initialize the buffer

    snprintf(buffer, IO_BUFFER_SIZE, "%s\n", data);  // Format the string
    printf("%s", buffer);

    free(buffer); // Free allocated memory
}

int main() {
    printLine("Hello, world!");
    printLine("This is another line.");
    return 0;
}
```