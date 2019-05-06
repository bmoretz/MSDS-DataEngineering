
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time
import matplotlib.style as style
from collections import deque, defaultdict

np.random.seed(323) # static seed so results are reproducible

characters = [chr(i) for i in range(97,123)] # character look-up

def gen_code():
    return ''.join([characters[int(np.random.uniform(0, 26))] for k in range(0, 10)]) # generate a random name

names = list() # names list

for index in range(25): # populate it
    names.append(gen_code())
    
assert set([x for x in names if names.count(x) > 1]) == set() # ensure no duplicates

nested_dict = lambda: defaultdict(nested_dict)
nest = nested_dict()

for index in [gen_code() for n in range(0, 5)]:
	nest[index] = [{k, k} for k in [gen_code() for n in range(0, 5)]]

	for i, j in enumerate(nest[index]):
		nest[i][j] = [{k, k} for k in [gen_code() for n in range(0, 5)]]

nest
