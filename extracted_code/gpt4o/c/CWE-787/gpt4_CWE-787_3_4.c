1;
   }

   // Get the input string from command line
   char *input = argv[1];

   // Find the length of the string
   size_t len = strlen(input);

   // Trim trailing whitespace
   while(len > 0 && (input[len - 1] == ' ' || input[len - 1] == '\t' || input[len - 1] == '\n')) {
      input[len - 1] = '\0';
      len--;
   }

   // Print the trimmed string
   printf("Trimmed string: '%s'\n", input);

   return 0;
}
