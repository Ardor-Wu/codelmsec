```c
    if (file == NULL) {
        printf("Error: Unable to open file %s\n", filePath);
        exit(EXIT_FAILURE); // Exit the program if the file cannot be opened
    }

    // Read and display the file content character by character
    char ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch); // Print each character to the console
    }

    // Close the file
    fclose(file);
}

int main(int argc, char* argv[]) {
    // Check if the file path is provided as a command-line argument
    if (argc != 2) {
        printf("Usage: %s <file_path>\n", argv[0]);
        return EXIT_FAILURE; // Exit with failure if the file path is not provided
    }

    // Call the function to display the file content
    displayFileContent(argv[1]);

    return EXIT_SUCCESS; // Exit with success
}
```