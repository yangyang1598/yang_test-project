//2번 코드


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
        printf("3개의 숫자선택:");
        for (int a = 0; a < 3; a++)
        {

            scanf_s("%d", &pa[a]);
            if (pa[a] > 9)
            {
                printf("다시 입력해주십시오:");
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

        printf("%d번째 도전 결과:%dstrike, %dball\n", cnt, strike, ball);
        cnt++;
    }
    printf("Game Over");
    _getch();
}