fileExists = true;
        fclose(file);
    }

    // If the file exists, include its contents
    if (fileExists) {
        printf("Including file: %s\n", filepath);
        file = fopen(filepath, "r");
        if (file == NULL) {
            perror("Error opening file");
            return;
        }

        char line[1024];
        while (fgets(line, sizeof(line), file) != NULL) {
            printf("%s", line); // Print each line of the file
        }

        fclose(file);
    } else {
        printf("File does not exist: %s\n", filepath);
    }
}

int main() {
    const char* filepath = "example.txt"; // Replace with the path to your file
    includeFile(filepath);
    return 0;
}
