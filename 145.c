#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    long i;
    int n, j;
    long r;
    char buf[12];
    char revbuf[12];

    int final = 0;
    for (i = 0; i < 1000000000; i++)
    {
        if (!(i % 10))
        {
            if (!(i % 1000000))
                printf("%d\n", i);
            continue;
        }
        n = sprintf(buf, "%ld", i);
        for (j = 0; j < n; j++)
            revbuf[j] = buf[n - 1 - j];
        r = strtol(revbuf, NULL, 10);
        r += i;

        n = sprintf(buf, "%ld", r);
        for (j = 0; j < n; j++)
        {
            if (!(buf[j] % 2))
                goto fail;
        }
        final++;
fail:
        continue;
    }

    printf("%d\n", final);
    return 0;
}
