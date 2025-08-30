import streamlit as st
import pandas as pd
import pickle

@st.cache_resource
def load_model():
    with open('crop_yield_model_full.pkl', 'rb') as f:
        model_data = pickle.load(f)
    return model_data

model_data = load_model()
model = model_data['model']
feature_columns = model_data['feature_columns']
categorical_columns = model_data['categorical_columns']

st.title("🌾 Crop Yield Prediction App")
st.write("Predict crop yield based on environmental and agricultural factors")

data = pd.read_csv("data.csv")
areas = sorted(data['Area'].unique())
items = sorted(data['Item'].unique())

year = st.number_input("Year", min_value=1990, max_value=2025, value=2010, step=1)
rainfall = st.number_input("Average Rainfall (mm/year)", min_value=0, value=1000)
pesticides = st.number_input("Pesticides (tonnes)", min_value=0, value=5000)
avg_temp = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=50.0, value=20.0, step=0.1)
area = st.selectbox("Country/Area", areas)
item = st.selectbox("Crop Item", items)

input_data = {
    'Year': year,
    'average_rain_fall_mm_per_year': rainfall,
    'pesticides_tonnes': pesticides,
    'avg_temp': avg_temp
}

for col in feature_columns:
    if col.startswith('Area_'):
        input_data[col] = 1 if area in col else 0
    elif col.startswith('Item_'):
        input_data[col] = 1 if item in col else 0
    elif col not in input_data:
        input_data[col] = 0

input_df = pd.DataFrame([input_data])
input_df = input_df[feature_columns]  

if st.button("Predict Yield"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"### Predicted Yield: {prediction:,.0f} hg/ha")
        
        st.subheader("Input Summary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Country:** {area}")
            st.write(f"**Crop:** {item}")
            st.write(f"**Year:** {year}")
        
        with col2:
            st.write(f"**Rainfall:** {rainfall} mm/year")
            st.write(f"**Pesticides:** {pesticides:,} tonnes")
            st.write(f"**Avg Temp:** {avg_temp}°C")
            
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
