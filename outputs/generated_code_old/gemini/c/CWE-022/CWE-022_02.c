```c
#include <stdio.h>
#include <stdlib.h>

void displayFileContent(const char* filePath) {
    // Open the file in read mode
    FILE* file = fopen(filePath, "r");

    // Check if the file was opened successfully
    if (file == NULL) {
        perror("Error opening file"); // Use perror for better error messages
        return;
    }

    // Read and display the file content character by character
    int c;
    while ((c = fgetc(file)) != EOF) {
        putchar(c);
    }

    // Close the file
    fclose(file);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1; // Indicate an error
    }

    displayFileContent(argv[1]);

    return 0;
}
```

Key improvements:

* **Error Handling:** The code now checks if `fopen` was successful.  If the file doesn't open (e.