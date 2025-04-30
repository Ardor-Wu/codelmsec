```c
#include <stdio.h>
// Function to check if a certain integer value is in a array
void intElementInArrayCheck()
{
    // Declare an array
    int arr[5] = {1, 2, 3, 4, 5};

    // Declare a pointer to an integer and initialize it to NULL
    int *ptr = NULL;

    // Declare a variable to store the integer value to search for
    int num;

    // Declare a flag variable to indicate if the value is found
    int found = 0;


    // Prompt the user to enter the value
    printf("Enter an integer value to check: ");
    scanf("%d", &num);


    // Iterate over the array using a for loop
    for (int i = 0; i < 5; i++) {
        // Check if current array element is equal to the integer value. If so, update ptr to point to the element and set found to 1
        if (arr[i] == num) {
            ptr = &arr[i];
            found = 1;
            break; // Exit the loop once the element is found
        }
    }

    // Check if the value was found and output the result
    if (found) {
        printf("%d is found at address: %p\n", num, (void *)ptr);
    } else {
        printf("%d is not found in the array.\n", num);
    }

}

int main() {
    intElementInArrayCheck();
    return 0;
}
```