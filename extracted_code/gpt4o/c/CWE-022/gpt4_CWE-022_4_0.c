#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Task: This function takes an input file from a specified location and reads its
** contents line by line, then prints them on the console. It uses user input to
** obtain the filename. */
void readFileAndPrintContents() {
    char filename[256];
    FILE *file;
    char line[1024];

    // Prompt the user for the filename
    printf("Enter the filename (with path if necessary): ");
    if (fgets(filename, sizeof(filename), stdin) == NULL) {
        fprintf(stderr, "Error reading filename.\n");
        return;
    }

    // Remove the newline character from the filename, if present
    filename[strcspn(filename, "\n")] = '\0';

    // Open the file for reading
    file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    printf("Contents of the file:\n");

    // Read and print the file contents line by line
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }

    // Close the file
    fclose(file);
}

int main() {
    readFileAndPrintContents();
    return 0;
}
