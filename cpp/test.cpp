#include <iostream>
#include <algorithm>
#include <chrono>
#include<vector>
using namespace std;
#include <time.h>
using namespace std::chrono; // @suppress("Symbol is not resolved")

int main() {
	vector<int> values(10000);
	 // Generate Random valuesf
	  auto f = []() -> int { return rand() % 10000; };

	  // Fill up the vector
	   generate(values.begin(), values.end(), f);

	  // Get starting timepoint
	   auto start = high_resolution_clock::now();


        int valeur=1;
        int somme=0;
	   for (int i = 0; i < 100000000; i++) {
		   somme=i+1;
		   if (somme%2==0){somme=somme+somme*somme;}
		   else {somme=somme-i*i;}
		   
	      }

	 // Get ending timepoint
	   auto stop = high_resolution_clock::now();

	
	   auto duration = duration_cast<microseconds>(stop - start);

	     cout << "Time taken by function: "
	          << float(duration.count()*0.000001) << " seconds" << endl;
			  cout << "fin du programme"<<endl;


}
