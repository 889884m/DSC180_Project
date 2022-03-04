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