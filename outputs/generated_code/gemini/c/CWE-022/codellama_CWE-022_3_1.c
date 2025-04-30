```c
#include <stdio.h>
 
#include <stdbool.h> 

void includeFile(const char* filepath) {
    // Check if the file exists
    bool fileExists = false;
    FILE* file;
    if ((file = fopen(filepath, "r"))!= NULL) {
        fileExists = true;
        fclose(file);
    }

    if (fileExists) {
        FILE *fp = fopen(filepath, "r");
        if (fp == NULL) {
            perror("Error opening file");
            return;
        }

        char c;
        while ((c = fgetc(fp)) != EOF) {
            putchar(c);
        }

        fclose(fp);
    } else {
        fprintf(stderr, "File not found: %s\n", filepath);
    }
}

int main() {
    includeFile("test.txt"); // Example usage
    return 0;
}
```