import sys
sys.path.append('../src')
import pickle
import numpy as np
from make_coords import load_coordinates

def load_data(path='../data/doa_proj2_allData.p'):
	doa2 = pickle.load(open(path,'rb'))
	coordinates = load_coordinates()
	cp_data = {cp: doa2[cp]['source0'].dropna(axis=1, how='all').iloc[600:1200, 1:].to_numpy() for cp in coordinates.keys()}
	X = np.vstack([cblock for cblock in cp_data.values()])
	y = np.vstack([np.full([cblock.shape[0], len(coordinates[cp])], coordinates[cp]) for cp, cblock in cp_data.items()])
	return X, y