//2�� �ڵ�


#include <stdio.h>
#include<time.h>
#include<stdlib.h>
int main()
{
    int com;
    int ca[3];
    int strike = 0, ball = 0;
    int pa[3];
    int cnt = 1;
    srand((unsigned)time(NULL));
    for (int j = 0; j < 3; j++)
    {
        ca[j] = rand() % 10;
        if (ca[j - 1] == ca[j])
        {
            ca[j] = rand() % 10;
           
        }
        else
            if (ca[j - 2] == ca[j])
            {
                ca[j] = rand() % 10;

            }

    }
     printf("Start Game!!\n");
    while (strike < 3)
    {
        strike = 0;
        ball = 0;
        printf("3���� ���ڼ���:");
        for (int a = 0; a < 3; a++)
        {

            scanf_s("%d", &pa[a]);
            if (pa[a] > 9)
            {
                printf("�ٽ� �Է����ֽʽÿ�:");
                a = 0;
            }
        }
        for (int a = 0; a < 3; a++)
        {
            for (int b = 0; b < 3; b++)
            {
                if (a == b)
                {
                    if (pa[a] == ca[b])
                    {
                        strike++;
                        break;
                    }
                }

                else
                {
                    if (pa[a] == ca[b])
                    {
                        ball++;
                        break;
                    }

                }
            }

        }

        printf("%d��° ���� ���:%dstrike, %dball\n", cnt, strike, ball);
        cnt++;
    }
    printf("Game Over");
    _getch();
}