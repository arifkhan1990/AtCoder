#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s1;
    int n, type,l, r;
    char ch;
    cin >> s1 >> n;
    while(n--) {
        cin >> type;
        if(type == 1) {
            cin >> ch >> l;
            s1[l] = ch;
        }else {
            cin >> ch >> l >> r;
            int ans = count(s1.begin()+l, s1.begin()+r+1, ch);
            cout << ans << endl;
        }
    }
    return 0;
}
