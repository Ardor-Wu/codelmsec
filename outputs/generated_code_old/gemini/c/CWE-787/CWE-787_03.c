```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    
    //make sure 1 argument was provided
    if (argc != 2) {
        printf("Need 1 argument\n");
        return 1; // Use return 1 for consistency
    }

    //get the argument
    char *input = argv[1];

    // Check if the input string contains only digits
    for (int i = 0; input[i] != '\0'; i++) {
        if (!isdigit(input[i])) {
            printf("Invalid input: Input must be a number.\n");
            return 1;
        }
    }


    // Convert the input string to an integer
    int num = atoi(input);


    // Example usage (replace with your desired logic)
    printf("The number entered is: %d\n", num);
    //  Now you can work with 'num' as an integer

    return 0;
}
```

Key improvements