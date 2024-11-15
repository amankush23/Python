import numpy as np
import joblib
import streamlit as st
import pandas as pd

model = joblib.load('demand_forecast_model.pkl')

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        width: 100%;
        padding: 10px 20px;
        font-size: 18px;
    }
    .stNumberInput input, .stSelectbox select {
        border-radius: 8px;
        border: 1px solid #ddd;
        padding: 10px;
        font-size: 16px;
    }
    .stTitle {
        color: #ff6347;
        text-align: center;
        font-weight: bold;
        font-size: 36px;
    }
    </style>
""", unsafe_allow_html=True)

st.title('🚀 Demand Forecast Predictor')

st.sidebar.header("🔧 Configuration")
selected_transport_mode = st.sidebar.selectbox('Select Transport Mode', 
                                               ['Bicycle', 'Bus', 'Car', 'Motorcycle', 
                                                'Ride-sharing', 'Taxi', 'Train', 'Walking'])

st.sidebar.write("Adjust the settings below for forecasting:")

col1, col2 = st.columns(2)

with col1:
    input_population_density = st.number_input('🌍 Population Density')
    input_economic_activity = st.number_input('📈 Economic Activity')

with col2:
    input_infrastructure_score = st.number_input('🏗️ Infrastructure Score', min_value=0.0, max_value=10.0, step=0.1)
    input_average_trip_length = st.number_input('🚗 Average Trip Length (km)')

modes = ['Bicycle', 'Bus', 'Car', 'Motorcycle', 'Ride-sharing', 'Taxi', 'Train', 'Walking']
mode_encoded = [1 if selected_transport_mode == mode else 0 for mode in modes]

input_data = pd.DataFrame(
    {
        'transport_mode_Bicycle': [mode_encoded[0]],
        'transport_mode_Bus': [mode_encoded[1]],
        'transport_mode_Car': [mode_encoded[2]],
        'transport_mode_Motorcycle': [mode_encoded[3]],
        'transport_mode_Ride-sharing': [mode_encoded[4]],
        'transport_mode_Taxi': [mode_encoded[5]],
        'transport_mode_Train': [mode_encoded[6]],
        'transport_mode_Walking': [mode_encoded[7]],
        'population_density': [input_population_density],
        'economic_activity': [input_economic_activity],
        'infrastructure_score': [input_infrastructure_score],
        'average_trip_length': [input_average_trip_length]
    }
)

expected_features = ['transport_mode_Bicycle', 'transport_mode_Bus', 'transport_mode_Car', 
                     'transport_mode_Motorcycle', 'transport_mode_Ride-sharing', 
                     'transport_mode_Taxi', 'transport_mode_Train', 'transport_mode_Walking',
                     'population_density', 'economic_activity', 
                     'infrastructure_score', 'average_trip_length']

input_data = input_data[expected_features]

if st.button('💡 Predict Demand'):
    demand_forecast = model.predict(input_data)
    
    st.success(f'🚚 **Predicted demand forecast**: {demand_forecast[0]:.2f} units')
else:
    st.write("Enter values and press **Predict** to see the demand forecast.")
