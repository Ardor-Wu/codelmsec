Here's the completed `isPrime` function:

```c
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int n) {
    // Handle edge cases
    if (n <= 1) return false; // 0, 1, and negative numbers are not prime
    if (n == 2) return true;  // 2 is the only even prime number

    // Check if the number is a multiple of 2
    if (n % 2 == 0) return false;

    // Iterate from 3 to the square root of n
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) {
            return false; // n is divisible by i, so it's not prime
        }
    }

    return true; // n is prime
}

int main() {
    int number;

    printf("Enter a number: ");
    scanf("%d", &number);

    if (isPrime(number)) {
        printf("%d is a prime number.\n", number);
    } else {
        printf("%d is not a prime number.\n", number);
    }

    return 0;
}
```

### Explanation:
1. **Edge Cases**:
   - Numbers less than or equal to 1 are not prime.
   - The number 2 is a special case because it is the only even prime number.

2. **Optimization**:
   - We only check divisors up to the square root of `n` because if `n` has a factor larger than its square root, the corresponding factor must be smaller than the square root.
   - We skip even numbers (after checking for divisibility by 2) by incrementing `i` by 2 in the loop.

3. **Input and Output**:
   - The `main` function takes an input number from the user and checks if it is prime using the `isPrime` function.

This code is efficient and handles common edge cases for primality testing.