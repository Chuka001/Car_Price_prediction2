import joblib
from regression_model.config.config import TRAINED_MODEL_DIR, FEATURES, PIPELINE_NAME
import pandas as pd
# from pathlib import Path

path = TRAINED_MODEL_DIR + '/' + PIPELINE_NAME

pipe = joblib.load(path)

def make_prediction(*, input_data) -> dict:
    """Make a prediction using a saved model pipeline.

    Args:
        input_data: Array of model prediction inputs.

    Returns:
        Predictions for each input row
    """

    data = pd.read_json(input_data)

    prediction = pipe.predict(data[FEATURES])


    results = {"predictions": prediction}

    return results