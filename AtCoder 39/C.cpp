#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,m,ar[1001];
    float ans;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> ar[i];
    }
    ans = ar[0];
    for(int i = 1; i < n; i++) {
        ans = (ans+ar[i])/2;
    }
    printf("%.6f\n",ans);
    return 0;
}
