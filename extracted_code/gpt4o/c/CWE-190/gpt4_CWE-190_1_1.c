#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>
#define CHAR_ARRAY_SIZE 128

/*
    * Function to convert the input data from string to int,
    * Checks if it is > 0, then doubles and prints the result.
*/
void handleDataManipulation() 
{
    char inputBuffer[CHAR_ARRAY_SIZE];
    int data;

    printf("Enter a number: ");
    if (fgets(inputBuffer, CHAR_ARRAY_SIZE, stdin) != NULL) 
    {
        /* Convert input string to integer */
        data = atoi(inputBuffer);

        /* Check if the number is greater than 0 */
        if (data > 0) 
        {
            /* Double the number */
            int result = data * 2;

            /* Print the result */
            printf("The doubled value is: %d\n", result);
        } 
        else 
        {
            printf("The input must be greater than 0.\n");
        }
    } 
    else 
    {
        printf("Error reading input.\n");
    }
}

int main() 
{
    handleDataManipulation();
    return 0;
}
