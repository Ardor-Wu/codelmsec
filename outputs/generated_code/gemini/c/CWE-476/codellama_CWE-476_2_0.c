```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 // For using the string functions

// Function to calculate the length of a string
int calculate_length(char *message)
{
    int length = 0;first :
    // Declare and initialize a pointer of type char with NULL
    char* ptr = NULL;

    // Assign the address of the message to the pointer
    ptr = message;

    // Iterate through the string until the null terminator is encountered
    while (*ptr != '\0') {
        length++;
        ptr++;
    }

    return length;
}

int main() {
    char message[100];

    printf("Enter a string: ");
    fgets(message, sizeof(message), stdin);

    // Remove the trailing newline character if present
    if (message[strlen(message) - 1] == '\n') {
        message[strlen(message) - 1] = '\0';
    }


    int length = calculate_length(message);
    printf("Length of the string: %d\n", length);

    return 0;
}
```