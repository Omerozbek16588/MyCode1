from sklearn.datasets import make_circles
from sklearn.cluster import DBSCAN

import matplotlib.pyplot as plt
import numpy as np

X, _ = make_circles(n_samples=400, factor=0.5, noise=0.05)

dbscan = DBSCAN(eps=0.1, min_samples=5)
labels = dbscan.fit_predict(X)

noise = np.where(labels == 1)
cluster = np.where(labels != 1)

plt.scatter(X[noise][:, 0], X[noise][:, 1], color = 'red', label = 'Gürültü', s = 50)
plt.scatter(X[cluster][:, 0], X[cluster][:, 1], c=labels[cluster], cmap='viridis', label = 'kümeler', s=50)
plt.title("DBSCAN ile Kümelerde Gürültü Oluşturma")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.show()