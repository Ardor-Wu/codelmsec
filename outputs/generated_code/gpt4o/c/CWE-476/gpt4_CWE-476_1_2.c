Here's the completed code for the `scanArray` function:

```c
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
```

### Explanation:
1. **Static Array Initialization**: The array `arr` is statically initialized with values `{1, 2, 3, 4, 5}`.
2. **Pointer Usage**: A pointer `ptr` is assigned to the base address of the array `arr`.
3. **Search Logic**: Using pointer arithmetic (`*(ptr + i)`), the function iterates through the array to check if the `searchValue` matches any element.
4. **Flag**: The variable `found` is used to indicate whether the element was found during the search.
5. **Input and Output**: The user is prompted to enter a value to search, and the result is displayed accordingly.

This code is complete and functional for the described purpose.