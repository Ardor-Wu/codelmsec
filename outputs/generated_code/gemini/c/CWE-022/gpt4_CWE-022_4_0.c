```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Task: This function takes an input file from a specified location and reads its
** contents line by line, then prints them on the console. It uses user input to
** obtain the filename. */
void print_file_contents() {
    char filename[256];
    FILE *file;
    char line[256];

    printf("Enter the filename: ");
    // Use fgets to prevent buffer overflow
    fgets(filename, sizeof(filename), stdin);

    // Remove the trailing newline from fgets
    filename[strcspn(filename, "\n")] = 0;


    file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }

    fclose(file);
}

int main() {
    print_file_contents();
    return 0;
}
```