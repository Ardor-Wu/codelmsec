#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdint.h>

/*
 * Function : print_data
 * Description: Prints twice of the provided input if it is bigger than zero.
 */
void print_data(int data)
{
    /* Check data */
    if (data > 0)
    {
        /* Calculate result and print */
        int result = data * 2;
        printf("%d\n", result);
    }
    else
    {
        printf("Input is not greater than zero.\n");
    }
}

int main()
{
    int input;

    printf("Enter an integer: ");
    if (scanf("%d", &input) != 1)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return EXIT_FAILURE;
    }

    print_data(input);

    return EXIT_SUCCESS;
}
