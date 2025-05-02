#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void splitFilePath(char* file_name) {
    FILE* file_pointer;
    char line_buffer[100];

    // Open the file if it exists
    if ((file_pointer = fopen(file_name, "r")) == NULL) {
        perror("Error opening file");
        return;
    }

    printf("Splitting file paths from file: %s\n", file_name);

    // Read each line from the file
    while (fgets(line_buffer, sizeof(line_buffer), file_pointer) != NULL) {
        // Remove newline character from the line
        line_buffer[strcspn(line_buffer, "\n")] = '\0';

        // Find the last occurrence of the '/' character
        char* last_slash = strrchr(line_buffer, '/');

        if (last_slash != NULL) {
            // Split into directory path and file name
            char directory_path[100];
            char file_name[100];

            strncpy(directory_path, line_buffer, last_slash - line_buffer);
            directory_path[last_slash - line_buffer] = '\0'; // Null-terminate the directory path

            strcpy(file_name, last_slash + 1); // Copy the file name

            printf("Directory: %s, File: %s\n", directory_path, file_name);
        } else {
            // If no '/' is found, the entire line is considered the file name
            printf("File: %s (No directory path)\n", line_buffer);
        }
    }

    // Close the file
    fclose(file_pointer);
}

int main() {
    char file_name[] = "file_paths.txt"; // Replace with your file name
    splitFilePath(file_name);
    return 0;
}
