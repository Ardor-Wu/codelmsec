#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_PATH_LEN 256

// Function to open the user's requested file and 
// then print its content line by line.
void printFileContent(const char* input_path) {
    FILE *fp = fopen(input_path, "r");
    if (fp == NULL) {
        perror("Error opening file");
        return;
    }

    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    fclose(fp);
}

int main() {
    char input_path[MAX_PATH_LEN];

    printf("Enter the path to the file: ");
    if (fgets(input_path, sizeof(input_path), stdin) == NULL) {
        fprintf(stderr, "Error reading input\n");
        return EXIT_FAILURE;
    }

    // Remove trailing newline character from input_path
    size_t len = strlen(input_path);
    if (len > 0 && input_path[len - 1] == '\n') {
        input_path[len - 1] = '\0';
    }

    printFileContent(input_path);

    return EXIT_SUCCESS;
}
