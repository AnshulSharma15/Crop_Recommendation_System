import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("crop_model.pkl", "rb"))

# Page settings
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# CSS
st.markdown("""
<style>

.stApp {
    background-image:
    linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
    url("https://images.unsplash.com/photo-1464226184884-fa280b87c399");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.block-container {
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

.main-box {
    background: rgba(0,0,0,0.45);
    padding: 40px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0,255,100,0.3);
    margin-top: 30px;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #76ff03;
}

.subtitle {
    text-align: center;
    color: white;
    font-size: 22px;
    margin-bottom: 40px;
}

.stNumberInput label {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold;
}

div[data-baseweb="input"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 12px;
}

.stButton>button {
    width: 100%;
    height: 70px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(to right, #00c853, #64dd17);
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 30px;
    box-shadow: 0px 0px 20px rgba(0,255,100,0.4);
}

.result {
    margin-top: 40px;
    background: rgba(0,0,0,0.5);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(0,255,100,0.3);
}

.result h2 {
    color: white;
    font-size: 30px;
}

.result h1 {
    color: #76ff03;
    font-size: 55px;
}

</style>
""", unsafe_allow_html=True)

# Main Box
# st.markdown('<div class="main-box">', unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">🌱 Crop Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Smart Farming Assistant</div>',
    unsafe_allow_html=True
)


# Columns
col1, col2 = st.columns(2)
with col1:

    N = st.number_input(
        "🌿 Nitrogen (N)",
        min_value=0,
        max_value=140,
        step=1
    )

    P = st.number_input(
        "🧪 Phosphorus (P)",
        min_value=5,
        max_value=145,
        step=1
    )

    K = st.number_input(
        "🍃 Potassium (K)",
        min_value=5,
        max_value=205,
        step=1
    )

    temperature = st.number_input(
        "🌡 Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        step=0.1
    )

with col2:

    humidity = st.number_input(
        "💧 Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        step=0.1
    )

    ph = st.number_input(
        "⚗ pH Value",
        min_value=0.0,
        max_value=14.0,
        step=0.1
    )

    rainfall = st.number_input(
        "🌧 Rainfall (mm)",
        min_value=0.0,
        max_value=400.0,
        step=0.1
    )
# Button
if st.button("🚀 Predict Best Crop"):

    data = np.array([[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]])

    prediction = model.predict(data)

    st.markdown(f"""
    <div class="result">
        <h2>🌾 Recommended Crop</h2>
        <h1>{prediction[0].upper()}</h1>
    </div>
    """, unsafe_allow_html=True)

# Close Box
# st.markdown('</div>', unsafe_allow_html=True)