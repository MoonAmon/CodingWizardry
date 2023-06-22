#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int num, base;
    printf("");
    scanf("%d",&num);
        
    for (int i = 0; base < num; i++)
    {
        if (num<0)
        {
            return false;
        }
        
        base=i*i;
        if (base==num)
        {
            return true;
            break;
        }
        
        
    }
    return false;

    

    return 0;
}
