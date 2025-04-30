```c
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
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin); // Use fgets to prevent buffer overflow

    // Remove trailing newline character from fgets
    str[strcspn(str, "\n")] = 0;


    int len = calculate_length(str);
    printf("Length of the string: %d\n", len);
    return 0;
}
```