```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 

int main()
{
    char path[256]; 
    char file_name[128];
    char buffer[255];
    FILE *fp;

    // Prompt user for file name
    printf("%s", "Enter the name of the file: ");
    fgets(file_name, sizeof(file_name), stdin);

    // Remove trailing newline from fgets
    file_name[strcspn(file_name, "\n")] = 0;


    // Construct the full path (assuming the file is in the current directory)
    snprintf(path, sizeof(path), "%s", file_name);


    // Open the file in read mode
    fp = fopen(path, "r");

    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Read and print the contents of the file line by line
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(fp);

    return 0;
}
```