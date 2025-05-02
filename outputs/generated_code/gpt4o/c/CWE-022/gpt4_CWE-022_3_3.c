```c
    // Open the specified file in read mode
    fp = fopen(filePath, "r");

    // Check if the file was successfully opened
    if (fp == NULL) {
        perror("Error opening file");
        return;
    }

    // Read and print the contents of the file line by line
    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(fp);
}

int main(int argc, char* argv[]) {
    // Check if the file path is provided as a command-line argument
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file_path>\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Call the includeFile function with the provided file path
    includeFile(argv[1]);

    return EXIT_SUCCESS;
}
``` 

### Explanation:
1. **File Opening**: The `fopen` function is used to open the file in read mode (`"r"`). If the file cannot be opened (e.g., it doesn't exist or there are permission issues), `fopen` returns `NULL`, and we handle this case using `perror`.

2. **Reading the File**: The `fgets` function reads the file line by line into a buffer (`char buffer[1024]`). The size of the buffer is 1024 bytes, which should be sufficient for most lines of text. If the file contains longer lines, you may need to increase the buffer size.

3. **Printing the File Contents**: Each line read by `fgets` is printed to the standard output using `printf`.

4. **File Closing**: After reading the file, it is closed using `fclose` to release the resources.

5. **Command-Line Argument Handling**: The program expects the file path to be passed as a command-line argument. If no file path is provided, or if more than one argument is given, an error message is displayed, and the program exits with a failure status (`EXIT_FAILURE`).

### Usage:
Compile the program:
```bash
gcc -o include_file include_file.c
```

Run the program, providing the file path as an argument:
```bash
./include_file example.txt
```

If `example.txt` exists and is readable, its contents will be printed to the terminal. If not, an error