#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to calculate the length of the string
int calculate_length(char *str) {
    int i = 0;
    // While str is not NULL, we keep on traversing 
    while (str[i] != '\0') {
        i++;
    }
    return i; // Return the length of the string
}

int main() {
    char str[100];
    
    // Prompt the user to enter a string
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remove the newline character added by fgets
    str[strcspn(str, "\n")] = '\0';
    
    // Calculate the length of the string
    int length = calculate_length(str);
    
    // Print the length of the string
    printf("The length of the string is: %d\n", length);
    
    return 0;
}
