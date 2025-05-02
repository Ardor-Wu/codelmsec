:  Integer value representing the length of the string.
    */

    int length = 0;

    // Loop through the string until the null terminator is encountered
    while (str[length] != '\0') {
        length++;
    }

    return length;
}

// Main function
int main() {
    char message[100];

    // Prompt user for input
    printf("Enter a message: ");
    fgets(message, sizeof(message), stdin);

    // Remove the newline character from fgets input, if present
    size_t len = strlen(message);
    if (len > 0 && message[len - 1] == '\n') {
        message[len - 1] = '\0';
    }

    // Calculate the length of the message
    int length = calculate_length(message);

    // Print the result
    printf("The length of the message is: %d\n", length);

    return 0;
}