#include <stdio.h>
#include <stdlib.h>

void removeBlankLines(char *);

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		printf("Need to have a file name in the arguments of this program\n");
		exit(0);
	}
	
	removeBlankLines(argv[1]);
	return 0;
}

void removeBlankLines(char *str)
{
	FILE *fp;
	fp = fopen(str,"r");
	if(fp == NULL)
	{
		printf("Error opening file.");
		exit(0);
	}
	char* buff = (char*) malloc(sizeof(char)*1000);
	char c = ' ';
	int len = 0;
	
	while(c != EOF)
	{
		c = fgetc(fp);
		printf("%c",c);		
	}
	printf("\n");
	c = ' ';
	rewind(fp);
	while(c != EOF)
	{
		c = fgetc(fp);
		if (buff[len-1] == '\n' && c == '\n')
			continue;
		buff[len] = c;
		len++;		
	}
	fputs(buff, stdout);
}
