```c
#include <stdio.h>
#include <stdlib.h>
 // for malloc

int main( int argc, char** argv )
{
    int size = 10; // or whatever
    char* buffer = (char*)malloc((size + 1) * sizeof(char));
    if( NULL == buffer )
    {
        perror("malloc failed"); // Print an error message
        return 1; // Indicate an error
    }

    // ... do something with buffer ...

    free(buffer); // Release the allocated memory
    buffer = NULL; // Good practice to prevent dangling pointers
    return 0;
}
```