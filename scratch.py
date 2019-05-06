
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

nested_dict = lambda: defaultdict(nested_dict)
graph = nested_dict()

def flatten(d, parent_key=''):
    items = []
    for k, v in d.items():
        try:
            items.extend(flatten(v, '%s%s_' % (parent_key, k)).items())
        except AttributeError:
            items.append(('%s%s' % (parent_key, k), v))
    return dict(items)

l2 = []
l3 = []
l4 = []
l5 = []

for i in [gen_code() for n in range(0, 5)]:
	for j in [gen_code() for n in range(0, 5)]:
		if len(l2) < 2:
			l2.append(j)
		for k in [gen_code() for n in range(0, 5)]:
			if len(l3) < 3:
				l3.append(k)
			for l in [gen_code() for n in range(0, 5)]:
				if len(l4) < 4:
					l4.append(l)
				for m in [gen_code() for n in range(0, 5)]:
					if len(l5) < 5:
						l5.append(m)
					graph[i][j][k][l][m] = [{k, k} for k in [gen_code() for n in range(0, 5)]]


l2
l3
l4
l5

graph

search_index = flatten(graph) # cache the search index

def search(name):
    search_queue = deque()
    search_queue += search_index # flatten keys to look-up
    # This array is how you keep track of which items you've searched before.
    searched = []
    while search_queue:
        item = search_queue.popleft() # Only search this item if you haven't already searched it.
        if item not in searched:
            if name in item:
                return True
            else:
                search_queue += graph[item]
                # Marks this item as searched
                searched.append(item)
    return False

search('nqxfvqfgqb')