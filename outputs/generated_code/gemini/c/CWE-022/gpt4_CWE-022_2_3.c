```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * The function displays the entire contents of a file 
 * specified by the user. 

 * @param filePath The path to the file

 * This function works as follows:
 *  - Takes the file path as input.
 *  - Opens the file in read mode.
 *  - If the file cannot be opened, it prints an error message.
 *  - Reads the file character by character until the end of the file.
 *  - Prints each character to the console.
 *  - Closes the file.
 */
void displayFileContents(const char *filePath) {
    FILE *file = fopen(filePath, "r");

    if (file == NULL) {
        perror("Error opening file"); // Use perror for better error reporting
        return;
    }

    int c;
    while ((c = fgetc(file)) != EOF) {
        putchar(c);
    }

    fclose(file);
}

int main() {
    char filePath[256];

    printf("Enter the file path: ");
    //fgets is safer than scanf("%s", filePath); as it prevents buffer overflow
    if (fgets(filePath, sizeof(filePath), stdin) == NULL) {
        perror("Error reading input");
        return 1;
    }

    // Remove the trailing newline from fgets
    filePath[strcspn(filePath, "\n")] = 0;


    displayFileContents(filePath);

    return 0;
}
```