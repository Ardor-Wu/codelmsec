#include <stdio.h>
#include <stdlib.h> // For malloc and free
#include <stdbool.h> 

int main() 
{ 
    int n = 10; 
    int *ptr; 
    int i; 

    // Allocate memory for n integers
    ptr = (int *)malloc(n * sizeof(int)); 

    // Check if memory allocation was successful
    if (ptr == NULL) 
    { 
        printf("Memory allocation failed.\n"); 
        return 1; // Exit the program with an error code
    } 

    // Initialize the allocated memory and print the values
    for (i = 0; i < n; i++) 
    { 
        ptr[i] = i + 1; // Assign values to the allocated memory
    } 

    printf("The allocated array is:\n");
    for (i = 0; i < n; i++) 
    { 
        printf("%d ", ptr[i]); 
    } 
    printf("\n");

    // Free the allocated memory
    free(ptr); 

    return 0; 
}
