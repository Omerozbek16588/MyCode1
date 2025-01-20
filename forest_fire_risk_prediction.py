import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, recall_score
import warnings

warnings.filterwarnings("ignore")

data = pd.DataFrame({
        "sicaklik": np.random.randint(30, 50, 100),
        "Nem": np.random.randint(30, 60, 100),
        "rüzgar_hizi": np.random.randint(1, 40, 100),
        "yangin_riski": np.random.choice([0, 1], 100)
        })

X = data[["sicaklik", "Nem", "rüzgar_hizi"]]
y = data["yangin_riski"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, criterion='gini', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk:", accuracy)

r2_scor = r2_score(y_test, y_pred)
print("r2 score:", r2_scor)

recall = recall_score(y_test, y_pred)
print("recall score:", recall)