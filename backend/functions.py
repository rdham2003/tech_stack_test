import ctypes
import os

# Load the shared library
# script_dir = os.path.dirname(os.path.abspath(__file__))
# lib_path = os.path.join(script_dir, 'libfactorial.so')
# lib = ctypes.CDLL(lib_path)

# lib.factorial.argtypes = [ctypes.c_int]
# lib.factorial.restype = ctypes.c_ulonglong

def factorial(num):
    if num == 0 or num == 1:
        return num
    else:
        return num * factorial(num-1)
    # return lib.factorial(num)

if __name__ == '__main__':
    print(factorial(5))
