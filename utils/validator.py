import pandas as pd                 
import joblib
import yaml
import os   
import streamlit as st               


def validate_columns(inputdata):
    
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
    
    inputdata_lower_columns = inputdata.columns.str.strip().str.lower().str.replace(" ", "_")
    missing_columns = [col for col in selected_columns if col not in inputdata_lower_columns]
    
    if missing_columns:
        return False, missing_columns
    return True, None


