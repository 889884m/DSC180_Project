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
models = {
	'linear regression': LinearRegression,
	'ridge': Ridge,
	'svr': SVR,
	'decision tree': DecisionTreeRegressor,
	'random forest': RandomForestRegressor,
	'xgb': XGBRegressor
}
predictions = {m: MultiOutputRegressor(m[1]()).fit(X, y).predict(X) for m, ax in zip(models.items(), axes)}
# %%
fig1, axes1 = plt.subplots(3, 2)
axes1 = axes1.flatten()
fig2, ax2 = plt.subplots()
[ax.scatter(*prediction.T, label=m) for ax, (m, prediction) in zip(axes1, predictions.items())]
[ax2.scatter(*prediction.T) for prediction in predictions.values()]
# %%
fig1.show()
fig2.show()