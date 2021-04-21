import pandas as pd
from pipeline import price_pipe
import joblib
from config.config import TRAINING_DATA_FILE, TARGET, FEATURES, TRAINED_MODEL_DIR, PIPELINE_NAME

from pipeline import price_pipe

def run_training() -> None:
    """Train the model."""

    # read training data
    data = pd.read_csv(TRAINING_DATA_FILE)

    features = data[FEATURES]
    target = data[TARGET]

    path = TRAINED_MODEL_DIR + PIPELINE_NAME

    price_pipe.fit(features, target)
    joblib.dump(price_pipe, path)    


if __name__ == "__main__":
    run_training()