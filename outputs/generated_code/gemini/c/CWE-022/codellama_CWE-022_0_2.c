```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 

void read_from_file(char *filename, char *buffer) {
    // Try to open the specified file in read-only and text mode
    FILE *file_pointer = fopen(filename, "r");

    // If file opening is unsuccessful, print an error message and exit
    if (file_pointer == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    // Seek to the end of the file to determine its size
    fseek(file_pointer, 0, SEEK_END);
    long file_size = ftell(file_pointer);

    // If the file is empty, close it and return
    if (file_size == 0) {
        fclose(file_pointer);
        return;
    }

    // Rewind the file pointer to the beginning of the file
    rewind(file_pointer);

    // Allocate memory to store the file contents, plus a null terminator
    buffer = (char *)malloc(sizeof(char) * (file_size + 1));

    // If memory allocation fails, print an error message, close the file, and exit
    if (buffer == NULL) {
        perror("Memory allocation failed");
        fclose(file_pointer);
        exit(EXIT_FAILURE);
    }


    // Read the entire file into the buffer
    size_t bytes_read = fread(buffer, sizeof(char), file_size, file_pointer);

    // Check if the number of bytes read matches the expected file size.
    if (bytes_read != file_size) {
        perror("Error reading file");
        free(buffer);  // Free the allocated memory
        fclose(file_pointer);
        exit(EXIT_FAILURE);
    }

    // Null-terminate the buffer to make it a valid C string
    buffer[file_size] = '\0';

    // Close the file pointer
    fclose(file_pointer);
}

int main() {
    char *buffer = NULL;
    read_from_file("example.txt", buffer);

    if (buffer != NULL) {
        printf("File content:\n%s\