#include<stdio.h>

void main()
{
	int a,b,c;
	printf("Enter A, B, C : ");
	scanf("%d%d%d",&a,&b,&c);
	printf("\nA = %d, B = %d, C = %d",a,b,c);
	
	if(a > b)
	{
		if(a > c)
		{
			printf("\nA is Greater");
		}
		else
		{
			printf("\n%C is Greater");
		}
	}
	else
	{
		if(b > c)
		{
			printf("\n%B is Greater");
		}
		else
		{
			printf("\n%C is Greater");
		}
	}
	
	
}