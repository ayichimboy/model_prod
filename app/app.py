 
import streamlit as st  
import pandas as pd 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.validator import validate_columns
from utils.predictor import make_predictions

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
st.title("ML Prediction App")

st.write("Upload a CSV file to generate predictions.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df.head())

    # Validate Columns
    valid, missing = validate_columns(df)

    if not valid:

        st.error(f"Missing required columns: {missing}")

    else:

        st.success("All required columns present")

        if st.button("Run Prediction"):

            results = make_predictions(df[selected_columns])
            results = results.astype(object)


            st.subheader("Prediction Results")

            st.dataframe(results)

            csv = results.to_csv(index=False)

            st.download_button(
                label="Download Predictions",
                data=csv,
                file_name="predictions.csv",
                mime="text/csv"
            )
