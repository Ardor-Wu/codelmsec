/* Multiply data function, it receives an integer, increments it by 1 and prints */
void multiply_data(unsigned int input)
{
    unsigned int result = (input + 1) * 2;
    printf("Result after incrementing and multiplying: %u\n", result);
}

int main()
{
    data_hybrid_t data;

    /* Initialize the union with an integer value */
    data.unionFirst = 42;

    /* Print the integer value stored in the union */
    printf("Initial integer value: %u\n", data.unionFirst);

    /* Print the byte representation of the integer */
    printf("Byte representation of the integer: ");
    for (size_t i = 0; i < sizeof(unsigned int); i++)
    {
        printf("%02X ", data.unionSecond[i]);
    }
    printf("\n");

    /* Call the multiply_data function with the integer value */
    multiply_data(data.unionFirst);

    return 0;
}
