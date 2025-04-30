```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 // for strlen function

int calculate_length(char *message)
{
    // Calculate length of the message (string)
    int length;
    length = strlen(message);
    return length;
}

int main()
{
    char first_message[] = "First";
    char second_message[] = "Second";
    char third_message[] = "Third";

    int first_length, second_length, third_length;

    first_length = calculate_length(first_message);
    second_length = calculate_length(second_message);
    third_length = calculate_length(third_message);


    printf("Length of the first message: %d\n", first_length);
    printf("Length of the second message: %d\n", second_length);
    printf("Length of the third message: %d\n", third_length);

    return 0;
}
```