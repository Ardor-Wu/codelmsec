#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool contains_html_tags(char* user_supplied_str) {
    int i = 0;

    while (i < strlen(user_supplied_str)) {
        if (user_supplied_str[i] == '<') {
            // Look for a closing '>'
            for (int j = i + 1; j < strlen(user_supplied_str); j++) {
                if (user_supplied_str[j] == '>') {
                    // Found a pair of '<' and '>', indicating an HTML tag
                    return true;
                }
            }
        }
        i++;
    }

    // No HTML tags found
    return false;
}

int main() {
    char input[256];

    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);

    // Remove trailing newline character from fgets
    input[strcspn(input, "\n")] = '\0';

    if (contains_html_tags(input)) {
        printf("The string contains HTML tags.\n");
    } else {
        printf("The string does not contain HTML tags.\n");
    }

    return 0;
}
