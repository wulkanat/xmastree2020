# conditional import

# TODO: set to false to use numpy instead of GPU accelerated cupy
CUDA = True

if CUDA:
    import cupy as np
else:
    pass
    import numpy as np
