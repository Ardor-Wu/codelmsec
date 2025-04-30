```c
#include <stdio.h>
 
#include <stdbool.h> 

int main() 
{ 
    // Declare the array 
    int arr[]= {1, 23, 2, 4, 2, 76, 2, 2, 1, 2};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Declare the element to be searched
    int x = 2;

    // Declare a flag variable
    bool found = false;

    // Iterate over the array
    for (int i = 0; i < n; i++) {
        // Check if the current element is equal to x
        if (arr[i] == x) {
            // If it is, set the flag variable to true
            found = true;

            // Print the index of the element
            printf("Element %d found at index %d\n", x, i);
        }
    }


    if (!found)
    {
        printf("Element %d not found in the array.\n", x);
    }


    return 0; 
}
```