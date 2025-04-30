```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
 

void print_data (int data) 
{
    char char_array[10];
    int i;
    /* FIX: Set the entire string to be printable. */
    for (i=0; i < 9; i++) {
        char_array[i] = ' ';
    }
    char_array[9] = '\0';

    sprintf(char_array, "%d", data);
    printf("%s\n", char_array);   
}

int main() {
    print_data(12345);
    print_data(0);
    print_data(-9876);
    return 0;
}
```