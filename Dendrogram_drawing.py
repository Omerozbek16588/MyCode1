from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

import matplotlib.pyplot as plt

X, _ = make_blobs(n_samples=200, centers=3, cluster_std=0.6, random_state=42)


linkage_methods = ["single", "ward", "average", "complete"]

plt.figure()
for i, linkage_method in enumerate(linkage_methods, 1):
    
    model = AgglomerativeClustering(n_clusters=3, linkage=linkage_method)
    cluster_labels = model.fit_predict(X)
    
    plt.subplot(2, 4, i)
    plt.title(f"{linkage_method.capitalize()} linkage Dendrogram") 
    dendrogram(linkage(X, method=linkage_method), no_labels=True)
    plt.xlabel('veri noktaları')
    plt.ylabel('uzaklık')
    
    plt.subplot(2, 4, i + 4)
    plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis')
    plt.title(f"{linkage_method.capitalize()} linkage Clustering")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()