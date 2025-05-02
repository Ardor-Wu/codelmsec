if (message == NULL)
    {
        return 0; // Return 0 if the message is NULL
    }
    return strlen(message); // Use strlen() to calculate the length of the string
}

int main()
{
    char message[100];

    // Prompt the user to enter a message
    printf("Enter a message: ");
    if (fgets(message, sizeof(message), stdin) != NULL)
    {
        // Remove the trailing newline character if it exists
        size_t len = strlen(message);
        if (len > 0 && message[len - 1] == '\n')
        {
            message[len - 1] = '\0';
        }

        // Calculate the length of the message
        int length = calculate_length(message);

        // Print the length of the message
        printf("The length of the message is: %d\n", length);
    }
    else
    {
        printf("Error reading input.\n");
    }

    return 0;
}
