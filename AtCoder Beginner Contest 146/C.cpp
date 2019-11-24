#include <bits/stdc++.h>
using namespace std;
long long int a, b,x, y;

int binarySearch()
{
  long long int lo = 0, hi = 1000000001;
  while(abs(lo - hi) > 1) {
  	long long int mid = (lo+hi)/2;
  	auto s = to_string(mid);
  	if(x >= (a*mid) + (b*s.size())) lo = mid;
  	else hi = mid;
  }
  return lo;
}
int main() {

	cin >> a >> b >> x;
	cout << binarySearch() << endl;
	return 0;
}
