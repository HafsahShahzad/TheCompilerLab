
#include <stdio.h>

int global_array[4] = {1, 2, 3, 4};

int compute(int n) {
    // Constant expressions (foldable)
    int a = 2 * 3;            // 6
    int b = 10 + 20;          // 30
    int c = (4 - 1) * (2 + 1); // 9

    // Memory operations
    int tmp = global_array[0] + global_array[1];
    global_array[2] = tmp + c;

    // Constant conditional (foldable)
    if (4 > 2)
        return a + b + c;     // branch known true
    else
        return tmp;
}

int main() {
    int res = compute(10);
    printf("Result: %d\n", res);
    return 0;
}
