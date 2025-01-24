import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=400, centers=4, cluster_std=0.6, random_state=42)

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

center = kmeans.cluster_centers_
labels = kmeans.labels_
 
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30, label="Veri Noktaları")
plt.scatter(center[:, 0], center[:, 1], c='red', marker='X', s=200, label="Küme Merkezleri")
plt.title('K-Means Kümeleme')
plt.xlabel('Özellik 1')
plt.ylabel('Özellik 2')
plt.legend()
plt.show()