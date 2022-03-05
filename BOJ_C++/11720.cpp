#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n;
	string num;
	int sum = 0;
	cin >> n;
	cin >> num;
	
	for (char c: num)
	{
		sum += c - '0'; // char to int
	}
	cout << sum;
	return 0;
};
