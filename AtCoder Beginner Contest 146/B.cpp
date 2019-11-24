#include <iostream>
using namespace std;

int main() {
	string ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ", s;
	int n;
	cin >> n >> s;
	for(int i = 0; i < s.size(); i++) {
		s[i] = ab[int(s[i]-'A')+n];
	}
	cout << s << endl;
	return 0;
}
