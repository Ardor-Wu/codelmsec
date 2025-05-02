// Read the entered filename from the user
    if (fgets(input_filename, sizeof(input_filename), stdin) == NULL) {
        fprintf(stderr, "Error reading filename.\n");
        return;
    }

    // Remove the newline character at the end of the input, if present
    size_t len = strlen(input_filename);
    if (len > 0 && input_filename[len - 1] == '\n') {
        input_filename[len - 1] = '\0';
    }

    // Construct the full path to the file (if needed, you can modify this logic)
    snprintf(data_path, sizeof(data_path), "./%s", input_filename);

    // Open the file for reading
    FILE *file = fopen(data_path, "r");
    if (file == NULL) {
        fprintf(stderr, "Error: Could not open file '%s'.\n", data_path);
        return;
    }

    // Read and display the contents of the file
    printf("Contents of the file '%s':\n", data_path);
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);
    printf("\nFile reading completed.\n");
}

int main() {
    display_input_file_contents();
    return 0;
}
