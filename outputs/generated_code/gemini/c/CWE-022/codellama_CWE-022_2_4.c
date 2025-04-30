```c
#include <stdio.h>
#include <stdlib.h>
 // For exit function

void displayFileContent(const char* filePath) {
    // Declare a file pointer
    FILE* file;

    // Open the given file in read mode
    file = fopen(filePath, "r");

    // Check whether the file exists
    if (file == NULL) {
        perror("Error opening file"); // Print an error message indicating the reason for failure
        exit(1); // Exit the program with a non-zero status code to indicate an error
    }

    // Declare a character to store each character read from the file
    char ch;

    // Read the file character by character until the end of file is reached
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch); // Print the character to the console
    }

    // Close the file
    fclose(file);
}
```