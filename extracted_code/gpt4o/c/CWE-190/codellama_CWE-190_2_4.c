#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>

void print_data(int data) 
{
    char char_array[10];
    int i;
    /* FIX: Set the entire string to be printable. */
    for (i = 0; i < 9; i++) {
        char_array[i] = 'A'; // Fill the array with a printable character
    }
    char_array[9] = '\0'; // Null-terminate the string

    /* Print the data */
    printf("Data: %d\n", data);
    printf("Char Array: %s\n", char_array);
}

int main() 
{
    int data = 42; // Example data
    print_data(data);
    return 0;
}
