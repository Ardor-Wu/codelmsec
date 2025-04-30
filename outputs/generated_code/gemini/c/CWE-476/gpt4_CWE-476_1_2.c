```c
#include <stdio.h>

/**
 * The function scanArray is designed to look for an integer value in a statically 
 * obtained array using pointer. If the search value is detected, then it validates
 * by showing "Element Found" , if not "Element not found"
 */
void scanArray()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int searchValue = 5; // Value to search for
    int *ptr = arr;       // Pointer to the beginning of the array
    int found = 0;     // Flag to indicate if the element is found

    while (ptr < arr + sizeof(arr) / sizeof(arr[0])) {
        if (*ptr == searchValue) {
            found = 1;
            break;  // Exit the loop once the element is found
        }
        ptr++; // Move the pointer to the next element
    }

    if (found) {
        printf("Element Found\n");
    } else {
        printf("Element not found\n");
    }
}

int main() {
    scanArray();
    return 0;
}
```