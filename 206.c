#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    char buf[20];
    unsigned long long i, s;
    int j;
    char found;
    for (i = 1010100000; i < 3162277662; i++)
    {
        found = 1;
        s = i * i;
        sprintf(buf, "%lld", s);
        if (!(i % 10000))
            printf("%lld, %lld\n", i, buf);
        for (j = 0; j < 10; j++)
        {
            if (buf[j * 2] - '0' != (j + 1) % 10)
            {
                found = 0;
                break;
            }
        }
        if (found)
        {
            printf("%lld, %lld\n", i, buf);
            break;
        }

    }
}

