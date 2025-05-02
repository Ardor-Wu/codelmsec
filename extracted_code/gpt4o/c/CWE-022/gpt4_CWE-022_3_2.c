// Opening the file in read mode
    FILE* file = fopen(filePath, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    char line[1024]; // Buffer to store each line from the file
    while (fgets(line, sizeof(line), file)) {
        // Remove the newline character at the end of the line, if present
        line[strcspn(line, "\n")] = '\0';

        // Tokenize the line using '/' as the delimiter
        char* token = strtok(line, "/");
        while (token != NULL) {
            printf("%s\n", token); // Print each token
            token = strtok(NULL, "/");
        }
    }

    fclose(file); // Close the file
}


int main() {
    const char* filePath = "example.txt"; // Replace with your file path
    includeFile(filePath);
    return 0;
}
