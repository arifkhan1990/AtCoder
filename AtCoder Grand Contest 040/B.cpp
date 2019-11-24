#include<bits/stdc++.h>
using namespace std;

using ll=long long;


int main()
{
    string s;
    long long ans = 0, n = 0, m = 0;
    cin >> s;
    int l = s.size();
    vector<int> a(l+1);
    for(int i = 0; i < l;i++) {
    	if(s[i] == '<' )a[i+1] = max(a[i + 1], a[i] + 1);
    }
    
    for(int i = l-1; i >=0 ;i--) {
    	if(s[i] == '>' )a[i] = max(a[i], a[i + 1] + 1);
    }
    
    for (int i = 0; i <= l; i++) {
        ans += a[i];
    }
    cout <<  ans << endl;
    return 0;
}