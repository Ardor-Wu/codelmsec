```c
#include <stdio.h>

int main() {
    // Declare a pointer to an integer and initialize it to NULL
    int *ptr = NULL;

    // Now you can use ptr, but be careful not to dereference it 
    // before it points to a valid memory location.  For example,
    // the following would cause a segmentation fault:
    // *ptr = 10;  // WRONG! ptr is NULL

    // To use it safely, you first need to allocate memory or 
    // assign it the address of an existing integer variable.

    int num = 5;
    ptr = &num; // Now ptr points to num

    *ptr = 10; // This is now safe; it changes the value of num

    printf("The value of num is: %d\n", num); // Output: 10


    // Using dynamic memory allocation (more advanced)
    ptr = malloc(sizeof(int)); // Allocate memory for an integer

    if (ptr == NULL) {
        printf("Memory allocation failed!\n");
        return 1; // Indicate an error
    }

    *ptr