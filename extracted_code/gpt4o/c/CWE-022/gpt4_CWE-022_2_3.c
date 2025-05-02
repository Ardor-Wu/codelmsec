#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * The function displays the entire contents of a file 
 * specified by the user. 
 *
 * @param filePath The path to the file
 *
 * This function works as follows:
 *  - The file is opened in read mode.
 *  - If the file cannot be opened, an error message is displayed.
 *  - The contents of the file are read and printed to the console.
 *  - The file is closed after reading.
 */
void displayFileContents(const char *filePath) {
    // Open the file in read mode
    FILE *file = fopen(filePath, "r");
    if (file == NULL) {
        // If the file cannot be opened, display an error message
        perror("Error opening file");
        return;
    }

    // Read and display the contents of the file
    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);
}

int main() {
    char filePath[256];

    // Prompt the user to enter the file path
    printf("Enter the path to the file: ");
    if (fgets(filePath, sizeof(filePath), stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return EXIT_FAILURE;
    }

    // Remove the trailing newline character from the input
    filePath[strcspn(filePath, "\n")] = '\0';

    // Display the contents of the file
    displayFileContents(filePath);

    return EXIT_SUCCESS;
}
