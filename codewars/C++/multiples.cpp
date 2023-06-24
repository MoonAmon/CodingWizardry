#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int sum;
    while (number>0)
    {
       if (number % 3 == 0 || number % 5 == 0)
       {
        sum+=number;
       }
       number-=1;
    }
    return sum;
}
