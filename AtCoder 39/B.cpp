#include<bits/stdc++.h>
using namespace std;

int main()
{

    int n, m, ar[1001];
    float ans = 0,res = 0;

    cin >> n >> ar[0];
    ans = ar[0];
    for(int i = 1; i < n; i++) {
        cin >> ar[i];
        ans = __gcd(ar[i-1], ar[i]);
    }
    for(int i = 0; i < n; i++) {
        res += ans/ar[i];
    }
    printf("%.7f\n",1/(res/ans));
    //cout << 1/(res/ans) << endl;
    return 0;
}
