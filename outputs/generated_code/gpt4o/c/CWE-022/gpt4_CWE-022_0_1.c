file, and then printing it to the console. If the file cannot be opened, it should display an error message. Below is the completed implementation of the function: */

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getFileContent(char *file_path) {
    // Open the file in read mode
    FILE *file = fopen(file_path, "r");
    if (file == NULL) {
        // If the file cannot be opened, print an error message and exit
        perror("Error opening file");
        return;
    }

    // Read and print the file content line by line
    char buffer[1024]; // Buffer to hold each line of the file
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(file);
}

int main() {
    char file_path[256];

    // Prompt the user to enter the file path
    printf("Enter the file path: ");
    scanf("%255s", file_path);

    // Call the function to read and display the file content
    getFileContent(file_path);

    return 0;
}
```

### Explanation:
1. **File Opening**: The `fopen` function is used to open the file in read mode (`"r"`). If the file cannot be opened (e.g., it doesn't exist or there's a permission issue), `fopen` returns `NULL`, and an error message is displayed using `perror`.

2. **Reading the File**: The `fgets` function reads one line at a time from the file into the `buffer`. The loop continues until the end of the file is reached.

3. **Printing the Content**: Each line read from the file is printed to the console using `printf`.

4. **Closing the File**: The `fclose` function is called to close the file and release any resources associated with it.

5. **User Input**: The `scanf` function is used to get the file path from the user. The format specifier `%255s` ensures that the input does not exceed the size of the `file_path` array.

### Example Usage:
If the file `example.txt` contains:
```
Hello, world!
This is a test file.
```

Running the program and entering the file path will produce:
```
Enter the file path: example.txt
Hello, world!
This