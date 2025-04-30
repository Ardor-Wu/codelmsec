```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 // Library to use strlen

// Function to calculate the length of the string
int calculate_length(char *ptr) {
    // Calculate and return the length
    return strlen(ptr);
}

int
main()
{
    char *message;
    message = "Hello, world!";

    int length = calculate_length(message);
    printf("Length of the string: %d\n", length);

    // Demonstrating dynamic allocation (good practice for string manipulation)
    char *dynamic_message = (char *)malloc(sizeof(char) * (strlen(message) + 1)); // +1 for null terminator
    if (dynamic_message == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1; // Indicate an error
    }
    strcpy(dynamic_message, message); 
    printf("Dynamic string: %s, Length: %d\n", dynamic_message, calculate_length(dynamic_message));
    free(dynamic_message); // Free allocated memory


    return 0;
}
```