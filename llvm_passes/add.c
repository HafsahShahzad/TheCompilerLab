
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int sum(int n) {
    int s = 0;
    for (int i = 0; i < n; i++)
        s += i;
    return s;
}

int main() {
    int x = add(1, 2);
    int y = sum(x);
    printf("%d\n", x);
    printf("%d\n", y);
    return 0;
}
