```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATH_LEN 256

int main() {
    char data_path[MAX_PATH_LEN];
    char input_filename[MAX_PATH_LEN];
    char full_path[MAX_PATH_LEN * 2]; // Increased size for combined path
    FILE *fp;

    // Get the data path from the user
    printf("Enter the data path: ");
    if (fgets(data_path, MAX_PATH_LEN, stdin) == NULL) {
        perror("Error reading data path");
        return 1;
    }

    // Remove trailing newline from fgets
    data_path[strcspn(data_path, "\n")] = 0;


    // Get the input filename from the user
    printf("Enter the input filename: ");
    if (fgets(input_filename, MAX_PATH_LEN, stdin) == NULL) {
        perror("Error reading input filename");
        return 1;
    }
    input_filename[strcspn