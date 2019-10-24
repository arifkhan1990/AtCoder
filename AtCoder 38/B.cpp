#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, ans = 0;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        string s;
        stringstream ss;
        ss << i;
        ss >> s;
        if(s.size()%2) ans++;
    }
    cout << ans << endl;
    return 0;
}
