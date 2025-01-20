from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings("ignore")

data = load_breast_cancer()

X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()

param_grid = {
    "criterion":['gini', 'entropy'],
    "n_estimators":[20, 50, 100],
    "max_depth":[None, 2, 5, 10],
    "min_samples_split":[2, 5, 10],
    "min_samples_leaf":[1, 2 ,4]
    }


grid_search = GridSearchCV(model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print("en iyi parametre:", best_params)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk (Accuracy):", accuracy)