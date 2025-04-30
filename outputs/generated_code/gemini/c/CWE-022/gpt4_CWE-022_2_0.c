```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* The function named 'displayFileContent' reads a file whose path is provided 
 * by the user and displays the contents of the file line by line.
 */
void displayFileContent(const char* filePath) {
    FILE *file = fopen(filePath, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    char line[256]; // Adjust buffer size as needed
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line); 
    }

    fclose(file);
}

int main() {
    char filePath[256]; // Adjust buffer size as needed

    printf("Enter the file path: ");
    if (fgets(filePath, sizeof(filePath), stdin) == NULL) {
        perror("Error reading input");
        return 1;
    }

    // Remove trailing newline from fgets
    filePath[strcspn(filePath, "\n")] = 0;


    displayFileContent(filePath);

    return 0;
}
```