```c
#include <stdio.h>
#include <stdlib.h>

// Function to determine if a value exists within an array
void findElementInArray()
{
    // declare and initialize array
    int arr[5] = {1, 2, 3, 4, 5};

    // Declares and initializes an integer pointer with NULL
    int *ptr = NULL;

    // declare and initialize search term
    int searchTerm = 3;

    // loop through the array
    for (int i = 0; i < 5; i++)
    {
        // Check if the current element matches the search term
        if (arr[i] == searchTerm)
        {
            // If a match is found, assign the address of the element to the pointer
            ptr = &arr[i];
            break; // Exit the loop once the element is found
        }
    }

    // Check if the pointer is still NULL (element not found)
    if (ptr == NULL)
    {
        printf("Element %d not found in the array.\n", searchTerm);
    }
    else
    {
        // If the pointer is not NULL, the element was found
        printf("Element %d found at address %p.\n", searchTerm, (void *)ptr);
        printf("Value at the address: %d\n", *ptr); // Dereference the pointer to print the value
    }
}

int main() {
    findElementInArray();
    return 0;
}
```