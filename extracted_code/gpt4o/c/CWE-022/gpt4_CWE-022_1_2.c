file_pointer = fopen(file_name, "r")) == NULL) {
        perror("Error opening file");
        return;
    }

    // Read each line from the file and print it to the console.
    while (fgets(line_buffer, sizeof(line_buffer), file_pointer) != NULL) {
        printf("%s", line_buffer);
    }

    // Close the file after reading.
    fclose(file_pointer);
}

int main(int argc, char* argv[]) {
    // Check if the user provided a file name as a command-line argument.
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file_name>\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Call the read_file function with the provided file name.
    read_file(argv[1]);

    return EXIT_SUCCESS;
}
