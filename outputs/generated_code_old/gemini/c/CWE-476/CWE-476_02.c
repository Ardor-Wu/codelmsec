```c
#include <stdio.h>

int main() {
    // Declares and initializes an integer array with values
    int arr[] = {1, 2, 3, 4, 5};

    // Calculate the size of the array (number of elements)
    int size = sizeof(arr) / sizeof(arr[0]);

    // Print the elements of the array
    printf("Elements of the array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");


    // Calculate the sum of the elements
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    printf("Sum of the elements: %d\n", sum);


    // Find the largest element
    int largest = arr[0];  // Initialize with the first element
    for (int i = 1; i < size; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
