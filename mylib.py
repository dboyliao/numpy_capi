# python wrapper file
import numpy as np
import numpy.ctypeslib as npct
import ctypes

arr_1d_type = npct.ndpointer(dtype=np.double, ndim=1, flags='CONTIGUOUS')
str_arr_type = npct.ndpointer(dtype='<S20', ndim=1, flags='CONTIGUOUS')

clib = npct.load_library("_libmylib.so", 'lib')
clib.cos_double.restype = None  # void
clib.cos_double.argtypes = [arr_1d_type, arr_1d_type, ctypes.c_size_t]
clib.print_strs.restype = None
clib.print_strs.argtypes = [str_arr_type, ctypes.c_size_t]


def cos_double(in_arr, out_arr=None):
    in_arr = in_arr.astype(np.double)
    if out_arr is None:
        out_arr = np.empty_like(in_arr)
    clib.cos_double(in_arr, out_arr, in_arr.size)
    return out_arr


def print_strs(in_arr):
    in_arr = np.array(in_arr, dtype='<S20')
    print(in_arr)
    clib.print_strs(in_arr, len(in_arr))
