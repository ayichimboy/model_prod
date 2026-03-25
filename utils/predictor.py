import joblib
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
config_file_path = BASE_DIR.parent / "config" / "config.yaml"

with open(config_file_path, "r") as f:
    config = yaml.safe_load(f)
    
model_path = BASE_DIR.parent / "classifier_model.pkl" 
model = joblib.load(model_path)

selected_columns = ['time(millisecond)', 'latitude', 'longitude',
       'height_above_takeoff(feet)',
       'height_above_ground_at_drone_location(feet)',
       'ground_elevation_at_drone_location(feet)',
       'altitude_above_sealevel(feet)', 'height_sonar(feet)', 'speed(mph)',
       'distance(feet)', 'mileage(feet)', 'satellites', 'gpslevel',
       'voltage(v)', 'max_altitude(feet)', 'max_ascent(feet)',
       'max_speed(mph)', 'max_distance(feet)', 'xspeed(mph)', 'yspeed(mph)',
       'zspeed(mph)', 'compass_heading(degrees)', 'pitch(degrees)',
       'roll(degrees)', 'isphoto', 'isvideo', 'rc_elevator', 'rc_aileron',
       'rc_throttle', 'rc_rudder', 'rc_elevator(percent)',
       'rc_aileron(percent)', 'rc_throttle(percent)', 'rc_rudder(percent)',
       'gimbal_heading(degrees)', 'gimbal_pitch(degrees)',
       'gimbal_roll(degrees)', 'battery_percent', 'current(a)',
       'battery_temperature(f)', 'altitude(feet)', 'ascent(feet)',
       'flycstateraw'
       ]

def make_predictions(inputdata, selected_columns=selected_columns, model=model):
    
    inputdata.columns = inputdata.columns.str.strip().str.lower().str.replace(" ", "_")
    inputdata_copied = inputdata.copy()
    
    inputdata_copied = inputdata_copied.loc[:,selected_columns]
    
    if selected_columns and model is not None:
           predictions = model.predict(inputdata_copied)
    return predictions