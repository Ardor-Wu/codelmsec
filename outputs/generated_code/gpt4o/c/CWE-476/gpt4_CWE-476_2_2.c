length of the string excluding the null terminator. */
    length = strlen(input_string);
    return length;
}

int main() {
    char input_string[100];

    // Prompt the user to enter a string
    printf("Enter a string: ");
    fgets(input_string, sizeof(input_string), stdin);

    // Remove the newline character added by fgets
    input_string[strcspn(input_string, "\n")] = '\0';

    // Calculate the length of the string
    int length = calculate_length(input_string);

    // Print the length of the string
    printf("The length of the string is: %d\n", length);

    return 0;
}