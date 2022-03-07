// Earliest possible day of full bloom
// link: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

#include <stdio.h>
#include <stdlib.h>

// A resposta comeÃ§a aqui
struct tempo
{
    int plant;
    int grow;
};

int cmp_grow(const void *a, const void *b)
{
    int x = ((struct tempo *)a)->grow;
    int y = ((struct tempo *)b)->grow;
    return (y - x);
}

int earliestFullBloom(int *plantTime, int plantTimeSize, int *growTime, int growTimeSize)
{
    struct tempo t[plantTimeSize];
    for (int i = 0; i < plantTimeSize; i++)
    {
        t[i].plant = plantTime[i];
        t[i].grow = growTime[i];
    }
    qsort(t, plantTimeSize, sizeof(struct tempo), cmp_grow);

    int day = -1, maxDay = 0;
    for (int i = 0; i < plantTimeSize; i++)
    {
        day += t[i].plant;
        if (maxDay <= (day + t[i].grow + 1))
            maxDay = (day + t[i].grow + 1);
    }
    return maxDay;
}
// A resposta termina aqui

int main()
{
    int n;
    int v1[100] = {};
    int v2[100] = {};

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &v1[i]);

    for (int i = 0; i < n; i++)
        scanf("%d", &v2[i]);
    printf("%d\n", earliestFullBloom(v1, n, v2, n));

    return 0;
}