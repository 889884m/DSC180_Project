import sys
sys.path.append('../src')
import pickle
import numpy as np

def load_coordinates():
	c1, c2 = np.array([173.5, 63]), np.array([55, 63])
	points = {
		'cp10': c1 + (-16, 10),
		'cp11': c1 + (-4, 0.5),
		'cp12': c1 + (-16.5, -10),
		'cp5': c2 + (3.5, 0.5),
		'cp6': c2 + (12.5, 11.5),
	}
	points['cp1'] =  points['cp12'] + (-27, -0.25)
	points['cp2'] =  points['cp1'] + (-24, 2)
	points['cp3'] =  points['cp2'] + (-27.5, -0.5)
	points['cp4'] =  points['cp3'] + (-14.5, -3)
	points['cp7'] =  points['cp6'] + (24, 2)
	points['cp8'] =  points['cp7'] + (16.5, 1.5)
	points['cp9'] =  points['cp8'] + (25.5, -2.5)
	return points

def load_data(path='../data/doa_proj2_allData.p'):
	doa2 = pickle.load(open(path,'rb'))
	coordinates = load_coordinates()
	cp_data = {cp: doa2[cp]['source0'].dropna(axis=1, how='all').iloc[600:1200, 1:].to_numpy() for cp in coordinates.keys()}
	X = np.vstack([cblock for cblock in cp_data.values()])
	y = np.vstack([np.full([cblock.shape[0], len(coordinates[cp])], coordinates[cp]) for cp, cblock in cp_data.items()])
	return X, y