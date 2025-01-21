from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt

digits = load_digits()

fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(10, 5))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="binary", interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(digits.target[i])
    
plt.tight_layout()
plt.show()

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("classification report:", classification_report(y_test, y_pred))







