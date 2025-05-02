```c
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
```

### Explanation:
1. **Escape Characters**:
   - `\n` is replaced with `\\n`.
   - `\t` is replaced with `\\t`.
   - `\\` is replaced with `\\\\`.

2. **Destination Buffer**:
   - The `dst` buffer must be large enough to hold the escaped string, which may be longer than the original string.

3. **Null-Termination**:
   - After processing the source string, the destination string is null-terminated to ensure it is a valid C string.

4. **Testing**:
   - The `main` function demonstrates the usage of the `escape_string` function and prints both the original and escaped strings.