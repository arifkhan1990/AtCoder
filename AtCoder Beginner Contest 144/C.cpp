#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long int n, ans = 0, i;
    cin >> n;
    for(i = 1; i <= sqrt(n); i++){
        if(n%i == 0) ans = (n/i) + i - 2;
    }
    cout << ans << endl;
    return 0;
}
