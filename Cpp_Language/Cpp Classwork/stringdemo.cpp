#include<iostream>

using namespace std;

int main()
{
	string kan = "Jay";
	string ishq = " Gohil";
	
	string str1;
	int len;
	
	//Kan = ishq;
	cout<<"\nKan = "<<kan;
	
	str1 = kan + ishq;
	cout<<"\nstring concatenate :"<<str1<<endl;
	
	len = ishq.size();
	cout<<"Length of ishq :"<<len;
	
	return 0;
}