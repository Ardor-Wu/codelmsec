```c
#include <stdio.h>
 
#include <stdbool.h>
#include <math.h>

bool isPrime(int n) {
    // Handle cases less than 2
    if (n <= 1) return false;

    // Check if the number is a multiple of 2
    if (n % 2 == 0) return n == 2; // 2 is prime

    // Iterate from 3 to the square root of n, checking odd numbers only
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) return false;
    }

    return true;
}
```