```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h> // Required for malloc

#define MAX_SIZE 256

char * copy_input(char *user_supplied_string){
    int i, dst_index;
    char *dst_buf = (char*)malloc(MAX_SIZE); // Allocate enough space

    if (dst_buf == NULL) {
        return NULL; // Handle memory allocation failure
    }

    dst_index = 0;
    for (i = 0; i < MAX_SIZE; i++) {
        if (user_supplied_string[i] == '\0') {
            break; // Stop copying at null terminator
        }
        dst_buf[dst_index++] = user_supplied_string[i];

        if (dst_index >= MAX_SIZE) {
            // Prevent buffer overflow if input is too large
            dst_buf[MAX_SIZE - 1] = '\0'; // Ensure null termination
            return dst_buf;
        }
    }
    dst_buf[dst_index] = '\0