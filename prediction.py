import joblib
def predict(Iris.csv):
    clf = joblib.load("rf_model.sav")
    return clf.predict(data)
