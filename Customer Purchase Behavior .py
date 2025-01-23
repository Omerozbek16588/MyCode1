from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
 

data = [
    [60000, 5, 0], [45000, 5, 1], [55000, 7, 0], [40000, 4, 1],
    [70000, 6, 0], [50000, 8, 1], [80000, 7, 0], [30000, 3, 1],
    [90000, 9, 0], [72000, 6, 0], [65000, 5, 0], [47000, 5, 1],
    [52000, 7, 0], [42000, 4, 1], [81000, 8, 0], [75000, 6, 0]
]

labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0]

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.33, random_state=42)

model = GaussianNB(var_smoothing=1e-9, priors=None)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cross_score = cross_val_score(model, data, labels, cv=5)
print("cross_val_score:", cross_score)