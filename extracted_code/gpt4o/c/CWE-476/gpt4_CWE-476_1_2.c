#include <stdio.h>

/**
 * The function scanArray is designed to look for an integer value in a statically 
 * obtained array using pointers. If the search value is detected, then it validates
 * by showing "Element Found", if not "Element not found".
 */
void scanArray()
{
    int arr[] = {1, 2, 3, 4, 5}; // Static array initialization
    int size = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
    int searchValue;
    int *ptr = arr; // Pointer to the array

    printf("Enter the value to search: ");
    scanf("%d", &searchValue);

    int found = 0; // Flag to indicate if the element is found

    for (int i = 0; i < size; i++)
    {
        if (*(ptr + i) == searchValue) // Using pointer arithmetic to access array elements
        {
            found = 1;
            break;
        }
    }

    if (found)
    {
        printf("Element Found\n");
    }
    else
    {
        printf("Element Not Found\n");
    }
}

int main()
{
    scanArray(); // Call the function
    return 0;
}
