from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

company = [
    "Apple", "Google", "Microsoft", "Pfizer", "Moderna",
    "Toyota", "BMW", "Ford", "JPMorgan", "Goldman Sachs",
    "BP", "ExxonMobil", "SpaceX", "Blue Origin", "Nvidia",
    "Amazon", "Intel", "Tesla", "Oracle", "Roche"
]
industrials = [
    "Technology", "Technology", "Technology", "Healthy", "Healthy",
    "Automotive", "Automotive", "Automotive", "Finance", "Finance",
    "Energy", "Energy", "Space", "Space", "Technology",
    "Technology", "Technology", "Automotive", "Technology", "Healthy"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(company)

X_train, X_test, y_train, y_test = train_test_split(X, industrials, test_size=0.33, random_state=42)

model = MultinomialNB(alpha=1.0)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk:", accuracy)