import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt

pd.set_option('display.precision', 15)

no_outliers = pd.read_csv('localization/no_outliers.txt', delimiter=' ', header = None, names = ['x', 'y'], skiprows=1)
with_outliers = pd.read_csv('localization/with_outliers.txt', delimiter=' ', header = None, names = ['x', 'y'], skiprows=1)
print("Files loaded")
#print(no_outliers.iloc[0])
#print(with_outliers.iloc[0])

X1 = no_outliers[['x','y']]
X2 = with_outliers[['x','y']]

X1_scaler=skl.preprocessing.StandardScaler()
X1_scaled=X1_scaler.fit_transform(X1)

X2_scaler=skl.preprocessing.StandardScaler()
X2_scaled=X2_scaler.fit_transform(X2)

print("Data scaled")

kmeans = skl.cluster.KMeans(n_clusters=5, random_state=40, n_init='auto')
kmeans.fit(X1_scaled)
no_outliers['cluster_label'] = kmeans.labels_
centroids1 = X1_scaler.inverse_transform(kmeans.cluster_centers_)
print("\n".join(str(x) for x in sorted(centroids1.tolist())))


kmeans = skl.cluster.KMeans(n_clusters=5, random_state=40, n_init='auto')
kmeans.fit(X2_scaled)
with_outliers['cluster_label'] = kmeans.labels_
centroids2 = X2_scaler.inverse_transform(kmeans.cluster_centers_)
print("\n".join(str(x) for x in sorted(centroids2.tolist())))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.scatter(no_outliers['x'], no_outliers['y'], c=no_outliers['cluster_label'], cmap='viridis', s=100)
ax1.scatter(centroids1[:, 0],
            centroids1[:, 1],
            marker='X', s=200, color='red', label='Centroids')
ax2.scatter(with_outliers['x'], with_outliers['y'], c=with_outliers['cluster_label'], cmap='viridis', s=100)
ax2.scatter(centroids2[:, 0],
            centroids2[:, 1],
            marker='X', s=200, color='red', label='Centroids')
ax1.set_title('With Outliers')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()
ax2.set_title('No Outliers')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.legend()
plt.tight_layout()
plt.show()