#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    long long int n , k, curr_idx = 0, first_idx = 0;
    cin >> n >> k;
    vector<long long int>ar;
    long long int data[n];
    for(int i = 0; i < n; i++) {
        cin >> data[i];
    }

    for(int i = 0; i < n*2; i++) {
      auto it = find(ar.begin(), ar.end(), data[i%n]);
    if (it != ar.end() ) {
              int x = it - ar.begin() + 1;
            ar.resize(x-1);
        }else {
            ar.push_back(data[i%n]);
        }
    }
    for(auto it = ar.begin(); it != ar.end(); it++) {
        cout << *it << " ";
    }
    return 0;
}
