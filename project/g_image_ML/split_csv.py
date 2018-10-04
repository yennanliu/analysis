# python 3 

import pandas as pd 
import numpy as np 


def index_marks(nrows, chunk_size):
    print ('chunk_size : ', chunk_size)
    return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)

def split(df, chunk_size):
    indices = index_marks(df.shape[0], chunk_size)
    return np.split(df, indices)
