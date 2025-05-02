It seems like your code snippet is incomplete and contains some syntax errors. I'll complete and correct it for you. Here's the corrected and completed version of your code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h> // for strlen function

int calculate_length(char *message)
{
    // Calculate length of the message (string)
    int length;
    length = strlen(message);
    return length;
}

int main()
{
    char *first = "First";
    char *second = "Second";
    char *third = "Third";

    printf("Length of '%s': %d\n", first, calculate_length(first));
    printf("Length of '%s': %d\n", second, calculate_length(second));
    printf("Length of '%s': %d\n", third, calculate_length(third));

    return 0;
}
```

### Explanation:
1. **`calculate_length` function**:
   - This function takes a string (`char *message`) as input and calculates its length using the `strlen` function from the `<string.h>` library.
   - It returns the length as an integer.

2. **Main function**:
   - Three strings (`first`, `second`, `third`) are defined and initialized.
   - The `calculate_length` function is called for each string, and the result is printed using `printf`.

### Output:
When you run the program, the output will be:
```
Length of 'First': 5
Length of 'Second': 6
Length of 'Third': 5
```