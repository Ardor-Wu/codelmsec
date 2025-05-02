#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void remove_char(char *str, char ch) {
    char *src, *dst;
    for (src = dst = str; *src != '\0'; src++) {
        *dst = *src;
        if (*src != ch) {
            dst++;
        }
    }
    *dst = '\0'; // Null-terminate the modified string
}

int main() {
    char str[100];
    char ch;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0'; // Remove the newline character from input

    printf("Enter the character to remove: ");
    scanf(" %c", &ch);

    remove_char(str, ch);

    printf("Modified string: %s\n", str);

    return 0;
}
