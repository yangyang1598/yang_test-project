//1���ڵ�

#include <stdio.h>
#include <stdlib.h>
int main()
{

    int** arr;//2���� �迭
    int size, size1, sum = 1;//�Է� ������ �� �ԷµǴ� ��
    int count = 0, z = 0, cnt = 1, ct = 0;//��� ������ ���߱� ���� ���� ����


    printf("����� �Է��Ͻÿ�:");
    scanf_s("%d", &size);
    arr = (int**)malloc(sizeof(int*) * size);
    size1 = size;

    for (int i = 0; i < size; i++)
    {
        arr[i] = (int*)malloc(sizeof(int) * size);

    }

    do {
        if (count % 2 == 0) {
            for (int i = z; i < size1; i++)
            {
                arr[z][i] = sum;
                sum++;

                if (i == size - cnt)
                {
                    cnt++;
                    for (int j = z + 1; j < size1; j++)
                    {
                        arr[j][i] = sum;
                        sum++;
                    }
                }
            }
            size1--;

            z++;


        }
        else
        {
            for (int i = size1 - 1; i >= z - 1; i--)
            {
                arr[size1][i] = sum;
                sum++;
                if (i == ct)
                {
                    ct++;
                    for (int j = size1 - 1; j >= z; j--)
                    {
                        arr[j][i] = sum;
                        sum++;
                    }
                }
            }


        }
        count++;
    } while (size1 >= 0);

    for (int a = 0; a < size; a++)
    {

        for (int b = 0; b < size; b++)
        {
            printf("%3d ", arr[a][b]);
        }
        printf("\n");
    }

    _getch();
}