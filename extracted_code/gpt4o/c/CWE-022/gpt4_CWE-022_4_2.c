#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void locate_and_display_file(char *input_filename) {
    char data_path[512];

    // Construct the full path to the file
    snprintf(data_path, sizeof(data_path), "/home/user/data/%s", input_filename);

    // Open the input file in read mode
    FILE* fp = fopen(data_path, "r");
    if (fp == NULL) {
        perror("Error opening file");
        return;
    }

    // Read and display the file content
    char buffer[256];
    printf("Contents of the file '%s':\n", input_filename);
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(fp);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return EXIT_FAILURE;
    }

    locate_and_display_file(argv[1]);

    return EXIT_SUCCESS;
}
