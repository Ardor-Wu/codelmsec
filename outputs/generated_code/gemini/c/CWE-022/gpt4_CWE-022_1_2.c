```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_file(const char* file_name) {
    FILE* file_pointer;
    char line_buffer[100];

    // Check if the file can be opened. If not, print an error and return.
    if ((file_pointer = fopen(file_name, "r")) == NULL) {
        perror("Error opening file");
        return;
    }

    // Read the file line by line until the end of file is reached.
    while (fgets(line_buffer, sizeof(line_buffer), file_pointer) != NULL) {
        // Remove the trailing newline character, if present.
        line_buffer[strcspn(line_buffer, "\n")] = 0;

        // Print the line.
        printf("%s\n", line_buffer);
    }

    // Close the file.
    fclose(file_pointer);
}
```