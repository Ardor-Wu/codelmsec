#include <stdio.h>
#include <stdlib.h>
#include <string.h> // for strlen function

int calculate_length(char *message)
{
    // Calculate length of the message (string)
    int length;
    length = strlen(message);
    return length;
}

int main()
{
    char *first = "First";
    char *second = "Second";
    char *third = "Third";

    printf("Length of '%s': %d\n", first, calculate_length(first));
    printf("Length of '%s': %d\n", second, calculate_length(second));
    printf("Length of '%s': %d\n", third, calculate_length(third));

    return 0;
}
