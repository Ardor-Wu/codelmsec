#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_from_file(char *filename, char *buffer, size_t buffer_size) {
    // Try to open the specified file in read-only and text mode
    FILE *file_pointer = fopen(filename, "r");

    // If file opening is unsuccessful, print an error message and exit
    if (file_pointer == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    // Read the contents of the file into the buffer
    size_t bytes_read = fread(buffer, 1, buffer_size - 1, file_pointer);
    if (ferror(file_pointer)) {
        perror("Error reading file");
        fclose(file_pointer);
        exit(EXIT_FAILURE);
    }

    // Null-terminate the buffer to make it a valid C string
    buffer[bytes_read] = '\0';

    // Close the file
    fclose(file_pointer);
}

int main() {
    char filename[256];
    printf("Enter the filename to read: ");
    scanf("%255s", filename);

    // Allocate a buffer to hold the file contents
    size_t buffer_size = 1024;
    char *buffer = malloc(buffer_size);
    if (buffer == NULL) {
        perror("Error allocating memory");
        return EXIT_FAILURE;
    }

    // Read the file contents into the buffer
    read_from_file(filename, buffer, buffer_size);

    // Print the file contents
    printf("File contents:\n%s\n", buffer);

    // Free the allocated memory
    free(buffer);

    return 0;
}
