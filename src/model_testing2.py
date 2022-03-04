# %%
import sys
sys.path.append('../src')
import pickle
import matplotlib.pyplot as plt
from data_processing.make_data import load_data

from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
# %%
V5 = pickle.load(open('../data/V5.p','rb'))
cp_list = V5["cp_list"]
active_L_table_slide_DOA = V5["active_L_table_slide_DOA"][:,6:]
active_L_table_slide_matrix = V5["active_L_table_slide_matrix"]
active_long_table_slide_DOA = V5["active_long_table_slide_DOA"][:,6:]
active_long_table_slide_matrix = V5["active_long_table_slide_matrix"]
X, y = load_data(path='../data/doa_proj2_allData.p')
# %%
fig, axes = plt.subplots(3, 2)
axes = axes.flatten()
# %%
models = {'linear regression': LinearRegression, 'ridge': Ridge, 'svr': SVR, 'decision tree': DecisionTreeRegressor, 'random forest': RandomForestRegressor, 'xgb': XGBRegressor}
for m, ax in zip(models.items(), axes):
	regr = MultiOutputRegressor(m[1]())
	regr.fit(X, y)
	plt.scatter(*regr.predict(X).T)
	# ax.scatter(*regr.predict(active_L_table_slide_DOA).T, label=m[0])
fig
# %%
