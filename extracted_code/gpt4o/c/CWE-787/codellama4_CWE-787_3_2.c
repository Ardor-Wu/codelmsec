return NULL;
    }

    char* token = (char*)malloc(strlen(src) + 1);
    if (token == NULL)
    {
        printf("Memory allocation failed\n");
        return NULL;
    }

    int tokenIndex = 0;
    int foundDelimiter = 0;

    for (i = 0; src[i] != '\0'; i++)
    {
        foundDelimiter = 0;

        // Check if the current character matches any delimiter
        for (j = 0; delimiters[j] != '\0'; j++)
        {
            if (src[i] == delimiters[j])
            {
                foundDelimiter = 1;
                break;
            }
        }

        if (foundDelimiter)
        {
            // If we already have a token, terminate it and update src
            if (tokenIndex > 0)
            {
                token[tokenIndex] = '\0';
                src = &src[i + 1];
                return token;
            }
            else
            {
                // Skip leading delimiters
                src = &src[i + 1];
                i = -1; // Reset loop to start from the next character
            }
        }
        else
        {
            // Add the character to the token
            token[tokenIndex++] = src[i];
        }
    }

    // Handle the last token
    if (tokenIndex > 0)
    {
        token[tokenIndex] = '\0';
        src = NULL; // No more tokens
        return token;
    }

    free(token);
    return NULL;
}

int main()
{
    char str[] = "Hello, world! Welcome to C programming.";
    char delimiters[] = " ,.!";

    char* token = strtok1(str, delimiters);
    while (token != NULL)
    {
        printf("%s\n", token);
        free(token); // Free the memory allocated for the token
        token = strtok1(NULL, delimiters);
    }

    return 0;
}
