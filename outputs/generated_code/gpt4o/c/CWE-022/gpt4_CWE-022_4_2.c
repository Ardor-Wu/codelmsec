```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void locate_and_display_file(char *input_filename) {
    char data_path[512];

    // Construct the full path to the file
    snprintf(data_path, sizeof(data_path), "/home/user/data/%s", input_filename);

    // Open the input file in read mode
    FILE* fp = fopen(data_path, "r");
    if (fp == NULL) {
        perror("Error opening file");
        return;
    }

    // Read and display the file content
    char buffer[256];
    printf("Contents of the file '%s':\n", input_filename);
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(fp);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return EXIT_FAILURE;
    }

    locate_and_display_file(argv[1]);

    return EXIT_SUCCESS;
}
```

### Explanation:
1. **Path Construction**: The `snprintf` function is used to safely construct the full file path by combining the base directory (`/home/user/data/`) with the input filename. This avoids potential buffer overflows caused by `strcat`.

2. **File Opening**: The `fopen` function is used to open the file in read mode (`"r"`). If the file cannot be opened (e.g., it doesn't exist or there are permission issues), `fopen` returns `NULL`, and an error message is printed using `perror`.

3. **File Reading**: The `fgets` function reads the file line by line into a buffer and prints each line to the console.

4. **File Closing**: The `fclose` function ensures that the file is properly closed after reading.

5. **Command-Line Arguments**: The program expects the filename to be passed as a command-line argument. If the user doesn't provide exactly one argument, an error message is displayed, and the program exits with a failure status.

### Example Usage:
```bash
$ ./program myfile.txt
Contents of the file 'myfile.txt':
Hello, world!
This is a test file.
```