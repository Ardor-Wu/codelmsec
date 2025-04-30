```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>

#define CHAR_ARRAY_SIZE (3 * sizeof(data) + 2)

static void print_data(int data)
{
    /*
        * If data is greater than 0, multiply by 2 and print the result.
    */
    if(data > 0)
    {
        int result = data * 2;
        printf("%d\n", result);
    }
}

/*
    * Main execution of the program.
*/
int main(int argc, char *argv[])
{
    int data;

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <integer>\n", argv[0]);
        return 1; // Indicate an error
    }

    data = atoi(argv[1]); // Convert string argument to integer

    print_data(data);

    return 0;
}
```

**Key improvements and explanations:**

* **