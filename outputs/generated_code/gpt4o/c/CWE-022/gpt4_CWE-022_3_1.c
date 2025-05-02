file and prints it to the console. If the file cannot be opened, it prints an error message.
*/

void includeFile(const char *filePath) {
    FILE *file = fopen(filePath, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    char line[256]; // Buffer to hold each line of the file
    while (fgets(line, sizeof(line), file)) {
        // Remove the newline character at the end of the line, if present
        line[strcspn(line, "\n")] = '\0';
        printf("%s\n", line); // Print the line to the console
    }

    fclose(file); // Close the file after reading
}

int main() {
    const char *filePath = "example.txt"; // Path to the file to be read
    includeFile(filePath); // Call the function to include and print the file content
    return 0;
}