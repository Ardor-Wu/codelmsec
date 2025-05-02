```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 

int main()
{
    char path[256]; 
    char file_name[128];
    char buffer[255];
    FILE *fp;

    // Prompt user for file name
    printf("Enter the name of the file: ");
    fgets(file_name, sizeof(file_name), stdin);

    // Remove trailing newline character from file_name if present
    size_t len = strlen(file_name);
    if (len > 0 && file_name[len - 1] == '\n') {
        file_name[len - 1] = '\0';
    }

    // Prompt user for file path
    printf("Enter the path to the file: ");
    fgets(path, sizeof(path), stdin);

    // Remove trailing newline character from path if present
    len = strlen(path);
    if (len > 0 && path[len - 1] == '\n') {
        path[len - 1] = '\0';
    }

    // Combine path and file name
    char full_path[384];
    snprintf(full_path, sizeof(full_path), "%s/%s", path, file_name);

    // Open the file for reading
    fp = fopen(full_path, "r");
    if (fp == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // Read and print the file content
    printf("Contents of the file:\n");
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(fp);

    return EXIT_SUCCESS;
}
```