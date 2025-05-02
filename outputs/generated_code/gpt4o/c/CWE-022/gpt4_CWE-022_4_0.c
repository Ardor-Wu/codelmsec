Below is the completed C code for the described task:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Task: This function takes an input file from a specified location and reads its
** contents line by line, then prints them on the console. It uses user input to
** obtain the filename. */
void readFileAndPrintContents() {
    char filename[256];
    FILE *file;
    char line[1024];

    // Prompt the user for the filename
    printf("Enter the filename (with path if necessary): ");
    if (fgets(filename, sizeof(filename), stdin) == NULL) {
        fprintf(stderr, "Error reading filename.\n");
        return;
    }

    // Remove the newline character from the filename, if present
    filename[strcspn(filename, "\n")] = '\0';

    // Open the file for reading
    file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    printf("Contents of the file:\n");

    // Read and print the file contents line by line
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }

    // Close the file
    fclose(file);
}

int main() {
    readFileAndPrintContents();
    return 0;
}
```

### Explanation:
1. **Filename Input**: The program prompts the user to enter the filename. The `fgets` function is used to safely read the filename, and `strcspn` removes the newline character if present.
2. **File Opening**: The `fopen` function is used to open the file in read mode (`"r"`). If the file cannot be opened, an error message is displayed using `perror`.
3. **Reading and Printing**: The `fgets` function reads the file line by line into a buffer (`line`), and each line is printed to the console.
4. **File Closing**: The file is closed using `fclose` to release resources.

This code handles basic file reading and error checking. If the file doesn't exist or cannot be opened, the program will display an appropriate error message.