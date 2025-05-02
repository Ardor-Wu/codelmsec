#include <stdio.h>
#include <stdlib.h>
#include <string.h> // For using the string functions

// Function to calculate the length of a string
int calculate_length(char *message)
{
    int length = 0;

    // Declare and initialize a pointer of type char with the address of the string
    char* ptr = message;

    // Traverse the string until the null terminator is reached
    while (*ptr != '\0') {
        length++;
        ptr++; // Move the pointer to the next character
    }

    return length;
}

int main()
{
    char message[100];

    printf("Enter a string: ");
    fgets(message, sizeof(message), stdin); // Read input from the user

    // Remove the newline character if it exists
    size_t len = strlen(message);
    if (len > 0 && message[len - 1] == '\n') {
        message[len - 1] = '\0';
    }

    int length = calculate_length(message);
    printf("The length of the string is: %d\n", length);

    return 0;
}
