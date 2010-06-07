#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define za 48
// zero in ascii

char valid(char *board)
{
    int ud, i, j, val, idx;
    char exists[9];

    // ud == up/down: ud == 0 -> row check, ud == 1 -> col check
    for (ud = 0; ud < 2; ud++)
    {
        for (i = 0; i < 9; i++)
        {
            memset(exists, 0, 9 * sizeof(char));
            for (j = 0; j < 9; j++)
            {
                idx = ud == 0 ? i * 9 + j : j * 9 + i;
                val = board[idx] - za;

                if (val < 0 || val > 9) // invalid board
                {
                    printf("invalid square value %d from %d at %d, %d\n", val, board[idx], i, j);
                    exit(-1);
                }
                if (val != 0)
                {
                    if (exists[val - 1]) // duplicate
                    {
                        //printf("duplicate value at %d, %d: %c\n", i, j, board[idx]);
                        return 0;
                    }
                    else
                        exists[val - 1] = 1;
                }
            }
        }
    }

    // subsquares
    for (i = 0; i < 9; i++)
    {
        // for each subsquare
        memset(exists, 0, 9 * sizeof(char));
        //    horizontal offset  + vertical offset
        idx = (i % 3) * 3        + (i / 3) * (3 * 9);
        for (j = 0; j < 9; j++)
        {
            // for each number within each subsquare
            idx = ((i % 3) * 3 + (i / 3) * (3 * 9)) +
                  ((j % 3) + (j / 3) * 9);

            val = board[idx] - za;
            if (val != 0)
            {
                if (exists[val - 1]) // duplicate
                {
                    //printf("duplicate value in subsquare phase at %d, %d: %c\n", i, j, board[idx]);
                    return 0;
                }
                else
                    exists[val - 1] = 1;
            }
        }
    }
    return 1;
}

char solve(char *board)
{
    int i, j;
    char done = 1;
    for (i = 0; i < 81; i++)
    {
        if (board[i] == 0 + za)
        {
            done = 0;
            for (j = 0; j < 9; j++)
            {
                board[i] = za + j + 1;
                if (!valid(board))
                    continue;
                if (solve(board))
                    return 1;
            }
            board[i] = 0 + za;
            return 0;
        }
    }
    if (valid(board))
        return 1;
}

int main(int argc, char **argv)
{
    FILE *input = fopen("96.data", "r");
    char linebuf[80];
    char board[82];

    int linelen = 0;
    int nline = 0;
    int sum = 0;

    while (fgets(linebuf, 80, input))
    {
        linelen = strlen(linebuf);
        if (linelen != 10)
        {
            if (linebuf[0] != 'G' && linebuf[0] != '\n')
                printf("invalid line: %s\n", linebuf);
            nline = 0;
        }
        else
        {
            strncpy(board + nline++ * 9, linebuf, 9);
        }
        if (nline == 9)
        {
            board[81] = '\0';
            /* Have a completed puzzle. Solve it. */
            solve(board);
            /* now calculate the sum of the top left 3 numbers */
            sum += 100 * (board[0] - za) + 10 * (board[1] - za) + (board[2] - za);
        }
    }

    printf("%d\n", sum);

    fclose(input);
    return 0;

}

