#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = n; i >= 1; i--)
	{
		// std::endl은 단순히 개행만 하는 것이 아닌 버퍼를 비우는 작업도 같이 하기 때문에
		// "\n"을 사용하는 것이 시간적인 면에서는 좋다.
		cout << i << "\n";
	}
	return 0;
};
