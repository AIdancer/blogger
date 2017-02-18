/*
1. How to use boost_regex.
   Following code is a piece of example. To compile it, you should link with "-lboost_regex -lboost_regex-mt" flag.
*/

#include <boost/regex.hpp>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	const char *str = "http://www.cppprog.com/2009/0112/48.html";
	boost::cmatch mat;
	boost::regex reg( "\\d+" );
	if(boost::regex_search(str, mat, reg))
	{
		cout << mat[0] << endl;
	}
	return  0;
}

