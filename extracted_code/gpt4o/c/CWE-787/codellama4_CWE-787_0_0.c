#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void escape_string(char *src, char *dst) {
    int dst_index = 0, i;

    for (i = 0; i < strlen(src); i++) {
        if (src[i] == '\n') {
            dst[dst_index++] = '\\';
            dst[dst_index++] = 'n';
        } else if (src[i] == '\t') {
            dst[dst_index++] = '\\';
            dst[dst_index++] = 't';
        } else if (src[i] == '\\') {
            dst[dst_index++] = '\\';
            dst[dst_index++] = '\\';
        } else {
            dst[dst_index++] = src[i];
        }
    }
    dst[dst_index] = '\0'; // Null-terminate the destination string
}

int main() {
    char src[] = "Hello\tWorld\nThis is a test\\string.";
    char dst[1024]; // Ensure the destination buffer is large enough

    escape_string(src, dst);

    printf("Original: %s\n", src);
    printf("Escaped: %s\n", dst);

    return 0;
}
