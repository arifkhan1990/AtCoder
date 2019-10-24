#include<stdio.h>

int sum(int arr[], int n) {
    int s = 0, i;
    for(i = 0; i < n; i++) {
        s += arr[i];
    }
    return s;
}
int main()
{
    int ar[] = {10,22,1,34,11};
    int ans = sum(ar, 0);
    printf("Sum = %d\n", ans);
    return 0;
}
