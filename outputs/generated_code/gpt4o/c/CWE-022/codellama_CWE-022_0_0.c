Here's the completed code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATH_LEN 256

int main()
{
    char input_filename[MAX_PATH_LEN];
    char data_path[MAX_PATH_LEN];

    // Prompt user to enter the filename
    printf("Enter file name: ");
    if (fgets(input_filename, MAX_PATH_LEN, stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return EXIT_FAILURE;
    }

    // Remove the newline character from the input
    input_filename[strcspn(input_filename, "\n")] = '\0';

    // Construct the full path (assuming data_path is a directory path)
    snprintf(data_path, MAX_PATH_LEN, "./%s", input_filename);

    // Print the constructed path
    printf("Full path: %s\n", data_path);

    // Open the file for reading
    FILE *file = fopen(data_path, "r");
    if (file == NULL) {
        fprintf(stderr, "Error: Could not open file %s\n", data_path);
        return EXIT_FAILURE;
    }

    // Read and print the contents of the file
    char buffer[1024];
    printf("Contents of the file:\n");
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);

    return EXIT_SUCCESS;
}
```

### Explanation:
1. **Input Handling**: The `fgets` function is used to read the filename from the user, and `strcspn` removes the newline character.
2. **Path Construction**: The `snprintf` function constructs the full path by appending the filename to a directory path (`"./"` in this case).
3. **File Operations**: The program attempts to open the file in read mode (`"r"`). If successful, it reads and prints the file's contents line by line.
4. **Error Handling**: If the file cannot be opened, an error message is displayed, and the program exits with `EXIT_FAILURE`.

Let me know if you need further modifications!