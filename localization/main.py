import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt
import numpy as np


pd.set_option('display.precision', 15)

with_outliers = pd.read_csv('./inferences.txt', delimiter=' ', header = None, names = ['x', 'y'], skiprows=1)
print("Files loaded")

X2 = with_outliers[['x','y']]

X2_scaler=skl.preprocessing.StandardScaler()
X2_scaled=X2_scaler.fit_transform(X2)
print("Data scaled")

dbscan = skl.cluster.DBSCAN(eps=0.2, min_samples=5)
dbscan.fit(X2_scaled)
with_outliers['cluster_label'] = dbscan.labels_

centroids2_df = with_outliers[with_outliers['cluster_label'] != -1].groupby('cluster_label')[['x','y']].mean()
if centroids2_df.empty:
    centroids2 = np.empty((0,2))
else:
    centroids2 = centroids2_df.sort_index().values

print("Centroids found")

with open("centers.out", "w") as f:
    for center in sorted(centroids2.tolist()):
        f.write(f"{round(center[0], 5)} {round(center[1], 5)}\n")