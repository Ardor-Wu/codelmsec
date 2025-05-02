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
