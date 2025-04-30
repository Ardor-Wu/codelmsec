```c
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <time.h>
#include <limits.h>
#include <string.h>
#include <stdint.h>

static const int STATIC_CONST_FIVE = 5;


void printHexCharLine(){
    
    char data;

    for (int i = 0; i < 16; i++) {
        data = (char)i;  // Cast to char to ensure correct printing
        if (i < 10) {
            printf("%X ", i); // Print hex value
        } else {
            printf("%X ", i); // Print hex value for A-F
        }

        // Printable ASCII characters are in the range 32-126 (inclusive)
        if (data >= 32 && data <= 126) {
            printf("%c ", data); // Print the character itself
        } else {
            printf(". "); // Print a dot for non-printable characters
        }
    }
    printf("\n");
}

int main