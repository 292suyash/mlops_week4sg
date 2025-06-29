import pickle
import json
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle

def train_and_save():
    X, y = load_iris(return_X_y=True)
    model = LogisticRegression()

    accuracy_over_epochs = []

    for epoch in range(5):
        X, y = shuffle(X, y)
        model.fit(X, y)
        preds = model.predict(X)
        acc = accuracy_score(y, preds)
        accuracy_over_epochs.append(acc)

    # Save model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    # Save metrics
    with open("metrics.json", "w") as f:
        json.dump({"accuracy": accuracy_over_epochs}, f)

if __name__ == "__main__":
    train_and_save()