```c
#include <stdio.h>
// The aim of the function is to look for a particular element in the array by using the pointer.
void searchData() {
    // Initialize an integer array
    int arr[] = {1, 2, 3, 4, 5};
    
    // Declares and initializes an integer pointer with
    int *ptr = arr;
    int key = 3; // Element to be searched
    int found = 0; // Flag to indicate if the element is found

    // Loop through the array using the pointer
    for (int i = 0; i < 5; i++) {
        if (*ptr == key) {
            printf("Element %d found at index %d\n", key, i);
            found = 1;
            break; // Exit the loop once the element is found
        }
        ptr++; // Move the pointer to the next element
    }

    if (!found) {
        printf("Element %d not found in the array\n", key);
    }
}

int main() {
    searchData();
    return 0;
}
```