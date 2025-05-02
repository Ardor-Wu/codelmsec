fopen(filePath, "r");
    if (file == NULL) {
        // Handle file open error
        perror("Error opening file");
        return;
    }

    // Read and print the contents of the file
    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        // Ensure the user provides a file path as an argument
        fprintf(stderr, "Usage: %s <file_path>\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Include the contents of the specified file
    includeFile(argv[1]);

    return EXIT_SUCCESS;
}
