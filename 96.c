#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define za 48
// zero in ascii

bool valid(char *board)
{
    int ud, i, j, val, idx;
    bool exists[9];

    // ud == up/down: ud == 0 -> row check, ud == 1 -> col check
    for (ud = 0; ud < 2; ud++)
    {
        for (i = 0; i < 9; i++)
        {
            memset(exists, 0, 9 * sizeof(bool));
            for (j = 0; j < 9; j++)
            {
                idx = ud == 0 ? i * 9 + j : j * 9 + i;
                val = board[idx] - za;
                if (ud == 0 && val == 0) //unsolved board
                {
                    printf("unsolved board\n");
                    return false;
                }
                else if (val < 0 || val > 9) // invalid board
                {
                    printf("invalid square value %d from %d at %d\n", val, board[idx], idx);
                    exit(-1);
                }
                if (exists[val - 1]) // duplicate
                {
                    printf("duplicate value at %d, %d: %c\n", i, j, board[idx]);
                    return false;
                }
                else
                    exists[val - 1] = true;
            }
        }
    }

    // subsquares
    for (i = 0; i < 9; i++)
    {
        // for each subsquare
        memset(exists, 0, 9 * sizeof(bool));
        //    horizontal offset  + vertical offset
        idx = (i % 3) * 3        + (i / 3) * (3 * 9);
        for (j = 0; j < 9; j++)
        {
            // for each number within each subsquare
            idx = ((i % 3) * 3 + (i / 3) * (3 * 9)) +
                  ((j % 3) + (j / 3) * 9);

            val = board[idx] - za;
            if (exists[val - 1]) // duplicate
            {
                printf("duplicate value in subsquare phase at %d, %d: %c\n", i, j, board[idx]);
                return false;
            }
            else
                exists[val - 1] = true;
        }
    }
    return true;
}

int main(int argc, char **argv)
{
    char board[82] = "534678912672195348198342567859761423426853791713924856961537284287419635345286179";
    if (valid(board))
        printf("yay\n");

    return 0;

}

