import pickle
import joblib

def score_model(df_features):
    
    scaler = joblib.load("app/models/scaler.pkl")

    with open("app/models/best_random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)

    X = df_features.drop(columns=["codmes", "CustomerKey"])
    X_scaled = scaler.transform(X)

    df_features["prediccion"] = model.predict(X_scaled)
    return df_features