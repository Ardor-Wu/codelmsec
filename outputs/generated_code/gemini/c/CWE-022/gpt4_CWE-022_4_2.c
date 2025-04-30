```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void locate_and_display_file(char *input_filename) {
    char data_path[512];

    // Open the input file in read mode
    strcpy(data_path, "/home/user/data/");
    strcat(data_path, input_filename);
    FILE* fp = fopen(data_path, "r");


    if (fp == NULL) {
        perror("Error opening file");
        return;
    }

    // Read and display the file content
    char ch;
    while ((ch = fgetc(fp)) != EOF) {
        putchar(ch);
    }

    // Close the file
    fclose(fp);
}
```