#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

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
        printf("%s\n", strs[i]);
    }
    printf("\n");
}

bool _is_overflow(u_int8_t a, u_int8_t b)
{
    if (a > UCHAR_MAX - b)
    {
        return true;
    }
    return false;
}

void to_gray(u_int8_t *img_data, u_int8_t *output, size_t n)
{
    for (size_t cnt = 0; cnt < n; ++cnt)
    {
        size_t off = cnt * 3;
        u_int8_t acc = 0;
        for (size_t i = 0; i < 3; ++i)
        {
            u_int8_t to_add = img_data[off + i];
            if (_is_overflow(acc, to_add))
            {
                acc = UCHAR_MAX;
                break;
            }
            else
            {
                acc += to_add / 3;
            }
        }
        output[cnt] = acc;
    }
}