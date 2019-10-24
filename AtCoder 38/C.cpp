#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    int vc[100001];
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> vc[i];
    }

    for(int i = n - 1; i > 0; i--) {
        if(vc[i] < vc[i-1]) vc[i - 1] -= 1;
    }

    for(int i = 1; i < n; i++) {
        if(vc[i-1] > vc[i]) return cout << "No" << endl, 0;
    }

    cout << "Yes" << endl;

    return 0;
}
