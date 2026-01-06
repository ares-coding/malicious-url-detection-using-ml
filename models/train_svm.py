import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

def train_svm():
    # Load processed features
    data = pd.read_csv("data/processed/features.csv")

    X = data.drop("label", axis=1)
    y = data["label"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train SVM model
    model = SVC(kernel="rbf", C=1.0, gamma="scale")
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Classification Report:\n")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:\n")
    print(confusion_matrix(y_test, y_pred))

    # Save model
    joblib.dump(model, "models/svm_model.pkl")
    print("\nModel saved as models/svm_model.pkl")

if __name__ == "__main__":
    train_svm()