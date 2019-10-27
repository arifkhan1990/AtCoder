#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a , b = 0;
    cin >> a;
    for(int  i = 1 ; i < 10; i++) {
        for(int j = 1; j < 10; j++) {
            if(i*j == a) {
                return cout << "Yes" << endl, 0;
            }
        }
    }
    cout << "No" << endl;
    return 0;
}
