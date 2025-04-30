```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
 * The function "removeTrailingNewLine" is a utility to sanitize a given 
 * string by removing trailing new line `\n`, carriage return `\r` and space ' ' characters.
 * It improves processing speed during character-based and pattern-based comparisons and prevent unexpected behavior because of these characters. 
 */

void removeTrailingNewLine(char *line) {
    if (line == NULL) {
        return;
    }

    int len = strlen(line);
    if (len == 0) {
        return;
    }

    while (len > 0 && (line[len - 1] == '\n' || line[len - 1] == '\r' || line[len - 1] == ' ')) {
        line[len - 1] = '\0';
        len--;
    }
}

int main() {
    char line1[] = "hello world\n";
    removeTrailingNewLine(line1);
    printf("Line 1: \"%s\"\n", line1);

    char line2[] = "hello world\r\n";
    removeTrailingNewLine(line2);
    printf("Line 2: \"%s\"\n", line2);

    char line3[] = "hello world   \n";
    removeTrailingNewLine(line3);
    printf("Line 3: \"%s\"\n", line3);


    char line4[] = "hello world";
    removeTrailingNewLine(line4);
    printf("Line 4: \"%s\"\n", line4);

    char *line5 = NULL;
    removeTrailingNewLine(line5);
    // No output, but no crash either


    char line6[] = "";
    removeTrailingNewLine(line6);
    printf("Line 6: \"%s\"\n", line6);


    return 0;
}
```