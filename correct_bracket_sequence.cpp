#include <iostream>
#include <cstring>

using namespace std;

int Catalan(int n)
{
  int C[n+1];
// storage array C[m]
  C[0]=1;
  for (int m=1; m<=n; ++m)   // calculate C[m] for m=1..n
  {
    C[m]=0;
    for (int k=0; k<m; ++k)
      C[m]+=C[k]*C[m-1-k];
  }
  return C[n];
}

int main(){
    int n;
    // while n<0 enter a non-negative integer
    do {
       cout << "number of brackets: ";
       cin >> n; // input number of brackets
       if (n<0) cout << "enter a non-negative integer! \n";
    } while (n<0);
    cout << "number of CBS: " << Catalan(n); // print result
    return 0;
}