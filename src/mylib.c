#include <math.h>
#include <stddef.h>
#include <stdio.h>

void cos_double(double *in_array, double *out_array, size_t size)
{
    for (size_t i = 0; i < size; ++i)
    {
        out_array[i] = cos(in_array[i]);
    }
}

void print_strs(char **strs, size_t size)
{
    for (size_t i = 0; i < size; ++i)
    {
        printf("%s, ", strs[i]);
    }
    printf("\n");
}