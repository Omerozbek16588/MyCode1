from sklearn.datasets import fetch_olivetti_faces
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

olivetti = fetch_olivetti_faces()

plt.figure()
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(olivetti.images[i], cmap='gray')
plt.show()

X = olivetti.data
y = olivetti.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("doğruluk:", accuracy)
