from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report

wine = load_wine()

X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_grid = {
    "kernel":['rbf', 'linear', 'poly'],
    "gamma":['scale', 'auto'],
    "C":[0.1, 1, 10]
    }

grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("en iyi parametreler:", grid_search.best_params_)
print("classification_report:", classification_report(y_test, y_pred))





