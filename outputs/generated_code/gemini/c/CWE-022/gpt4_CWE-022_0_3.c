```c
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

    char line[MAX_PATH_LEN];
    while (fgets(line, sizeof(line), fp) != NULL) {
        printf("%s", line);
    }

    fclose(fp);
}

int main() {
    char input_path[MAX_PATH_LEN];

    printf("Enter the path to the file: ");
    if (fgets(input_path, sizeof(input_path), stdin) == NULL) {
        perror("Error reading input");
        return 1;
    }

    // Remove trailing newline from fgets
    input_path[strcspn(input_path, "\n")] = 0;


    printFileContent(input_path);

    return 0;
}
```