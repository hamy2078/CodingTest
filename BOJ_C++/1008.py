#include <iostream>

using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	// 절대오차 또는 상대오차가 10^-9이하
	//fixed 는 소숫점 이하의 숫자만 다루도록 함
	// precision은 몇 자리의 숫자를 나타낼 것인지 지정함
	cout << fixed;
	cout.precision(9);
	cout << a / double(b);
	return 0;
};
