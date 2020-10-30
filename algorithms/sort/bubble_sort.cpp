/*
  Bubble sort implementation using CPP14 STL
  https://en.wikipedia.org/wiki/Bubble_sort
  Worst-case performance: O(N^2)

*/

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void swapi (int *a, int *b)
{
  int t = *a;
  *a = *b;
  *b = t;
}

vector <int> BubbleSort (vector <int>arr, int n)
{
  int i, j;
  bool te;
  for (i = 0; i < n; i++)
    {
      te = false;
      for (j = 0; j < n - 1 - i; j++)
	{
	  if (arr[j] > arr[j + 1])
	    {
	      swapi (&arr[j], &arr[j + 1]);
	      te = true;
	    }
	}
      if (te == false)
        break;
  }
  return arr;
}

int
main ()
{
  std::vector <int>vec;
  vec = {202, 4, -5, 66, -2, 0, 96, 5, 78, 12, 48, 88};
  vec = BubbleSort(vec , vec.size());
  // Printting the sorted vector
  for (int x:vec)
      cout << x << " ";
  return 0;
}
