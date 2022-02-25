# %%
import numpy as np
# %%
def load_coordinates():
	c1, c2 = np.array([173.5, 63]), np.array([55, 63])
	points = {
		10: c1 + (-16, 10),
		11: c1 + (-4, 0.5),
		12: c1 + (-16.5, -10),
		5: c2 + (3.5, 0.5),
		6: c2 + (12.5, 11.5),
	}
	points[1] =  points[12] + (-27, -0.25)
	points[2] =  points[1] + (-24, 2)
	points[3] =  points[2] + (-27.5, -0.5)
	points[4] =  points[3] + (-14.5, -3)
	points[7] =  points[6] + (24, 2)
	points[8] =  points[7] + (16.5, 1.5)
	points[9] =  points[8] + (25.5, -2.5)
	return points