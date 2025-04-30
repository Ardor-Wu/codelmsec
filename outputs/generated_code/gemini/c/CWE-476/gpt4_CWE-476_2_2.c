```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Function to calculate the length of a string
int calculate_length(char *input_string) {
    // We would use the strlen() function from the standard C library string.h
    int length = 0; 

    /* We call strlen(char_array) where char_array is the C 
       string, which returns the */
    length = strlen(input_string);
    return length;
}


int main() {
    char my_string[] = "Hello, world!";
    int len = calculate_length(my_string);
    printf("The length of the string is: %d\n", len);
    return 0;
}
```