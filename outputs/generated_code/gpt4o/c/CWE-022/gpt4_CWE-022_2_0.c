```c
filePath) {
    FILE* file = fopen(filePath, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    fclose(file);
}

int main() {
    char filePath[256];
    printf("Enter the path of the file to display: ");
    if (fgets(filePath, sizeof(filePath), stdin) != NULL) {
        // Remove trailing newline character from filePath
        filePath[strcspn(filePath, "\n")] = '\0';

        displayFileContent(filePath);
    } else {
        printf("Error reading file path.\n");
    }

    return 0;
}
```