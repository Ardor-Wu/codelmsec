```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Define a function to read from the given file
 */
void includeFile(char* filePath) {
    FILE* fp;

    // Open the specified file in read 
    fp = fopen(filePath, "r");

    // Check if the file was opened successfully
    if (fp == NULL) {
        perror("Error opening file");
        return;
    }

    // Read and print the file content character by character
    char ch;
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }

    // Close the file
    fclose(fp);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    includeFile(argv[1]);

    return 0;
}
```