#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getFileContent(char *file_path) {
    // Open the file in read mode
    FILE *file = fopen(file_path, "r");
    if (file == NULL) {
        // If the file cannot be opened, print an error message and exit
        perror("Error opening file");
        return;
    }

    // Read and print the file content line by line
    char buffer[1024]; // Buffer to hold each line of the file
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);
}

int main() {
    char file_path[256];

    // Prompt the user to enter the file path
    printf("Enter the file path: ");
    scanf("%255s", file_path);

    // Call the function to read and display the file content
    getFileContent(file_path);

    return 0;
}
