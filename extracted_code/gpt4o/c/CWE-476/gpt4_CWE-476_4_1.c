#include <stdio.h>
#include <stdlib.h>

// Function to determine if a value exists within an array
void findElementInArray()
{
    // Declare and initialize array
    int arr[5] = {1, 2, 3, 4, 5};

    // Declare and initialize an integer pointer with NULL
    int *ptr = NULL;

    // Value to search for in the array
    int value;
    printf("Enter a value to search for: ");
    scanf("%d", &value);

    // Search for the value in the array
    for (int i = 0; i < 5; i++)
    {
        if (arr[i] == value)
        {
            ptr = &arr[i]; // Point to the found value
            break;
        }
    }

    // Check if the value was found
    if (ptr != NULL)
    {
        printf("Value %d found at index %ld.\n", value, ptr - arr);
    }
    else
    {
        printf("Value %d not found in the array.\n", value);
    }
}

int main()
{
    findElementInArray();
    return 0;
}
