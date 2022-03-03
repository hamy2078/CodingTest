#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

int main()
{
	int n;
	int scores[1001] = { 0 }; // 배열의 크기 설정
	int max;
	double mean = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> scores[i];
	}
	max = *max_element(scores,scores+n); //배열에서 max값 찾기

	for (int i = 0; i < n; i++)
	{
		mean += scores[i]/(double)max*100;
	}
	cout << mean/n;
	return 0;
};
