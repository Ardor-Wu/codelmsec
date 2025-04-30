```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_file(char *file_name) {
  char line_buffer[100];
  FILE *file_pointer;

  // Try to open the file in read-only mode
  file_pointer = fopen(file_name, "r");

  // Check if the file was opened successfully
  if (file_pointer == NULL) {
    perror("Error opening file"); // Use perror for better error messages
    return; // Exit the function if the file cannot be opened
  }

  // Read the file line by line
  while (fgets(line_buffer, sizeof(line_buffer), file_pointer) != NULL) {
    // Remove the trailing newline character, if present
    line_buffer[strcspn(line_buffer, "\n")] = 0; 

    printf("%s\n", line_buffer);
  }

  // Close the file
  fclose(file_pointer);
}

int main() {
  char file_name[100];

  printf