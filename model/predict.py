import pickle
import pandas as pd

# 1. Load the trained ML model in Read-Binary ('rb') mode
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

class_labels = model.classes_.tolist()
def predict_output(user_input : dict):
    df = pd.DataFrame([user_input])
    predicted_class = model.predict(df)[0]
    probalities = model.predict_proba(df)[0]
    confidence = max(probalities)
    class_probs = dict(zip(class_labels , map(lambda p : round(p , 4),probalities)))

    return {
         "predicted_category": predicted_class , 
         "confidence" : round(confidence , 4 ),
         "class_probalities" : class_probs

    }

# def predict_output(user_input : dict):
#     input_df = pd.DataFrame([user_input])
#     output = model.predict(input_df)[0]
#     return output 
