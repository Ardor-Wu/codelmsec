#include <stdio.h>
#include <string.h>

void preventScriptInjection(char user_supplied_string[], char dst_buf[]) {
    int MAX_SIZE = 500;
    int dst_index = 0;

    for (int i = 0; user_supplied_string[i] != '\0'; i++) {
        if (user_supplied_string[i] == '&') {
            // Check if adding "&amp;" would exceed the buffer size
            if (dst_index + 5 >= MAX_SIZE) {
                printf("Error: Destination buffer overflow prevented.\n");
                dst_buf[dst_index] = '\0'; // Null-terminate the buffer
                return;
            }
            // Replace '&' with "&amp;"
            strcpy(&dst_buf[dst_index], "&amp;");
            dst_index += 5; // Move the index forward by the length of "&amp;"
        } else {
            // Check if adding a single character would exceed the buffer size
            if (dst_index + 1 >= MAX_SIZE) {
                printf("Error: Destination buffer overflow prevented.\n");
                dst_buf[dst_index] = '\0'; // Null-terminate the buffer
                return;
            }
            // Copy the character as is
            dst_buf[dst_index] = user_supplied_string[i];
            dst_index++;
        }
    }

    // Null-terminate the destination buffer
    dst_buf[dst_index] = '\0';
}

int main() {
    char user_input[] = "Hello & welcome to the world of C & programming!";
    char sanitized_output[500];

    preventScriptInjection(user_input, sanitized_output);

    printf("Sanitized Output: %s\n", sanitized_output);

    return 0;
}
