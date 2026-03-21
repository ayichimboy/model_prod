import joblib
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
config_file_path = BASE_DIR.parent / "config" / "config.yaml"

with open(config_file_path, "r") as f:
    config = yaml.safe_load(f)
    
model_path = BASE_DIR.parent / "classifier_model.pkl" 
model = joblib.load(model_path)

def make_predictions(inputdata, model=model):
    predictions = model.predict(inputdata)
    
    return predictions