# import streamlit as st
# import numpy as np
# import pickle
# import os

# # ===============================
# # Load model
# # ===============================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(BASE_DIR, "model.pkl")

# with open(model_path, "rb") as f:
#     model = pickle.load(f)


# # ===============================
# # Page config
# # ===============================
# # st.set_page_config(
# #     page_title="Restaurant Popularity Predictor",
# #     page_icon="🍽️",
# #     layout="centered"
# # )

# # ===============================
# # Custom Glass UI Style
# # ===============================
# st.markdown("""
# <style>
# .stApp {
#     background: linear-gradient(135deg, #1f4037, #99f2c8);
# }

# .card {
#     background: rgba(255,255,255,0.15);
#     backdrop-filter: blur(12px);
#     border-radius: 20px;
#     padding: 25px;
#     box-shadow: 0 8px 32px rgba(0,0,0,0.25);
# }

# .title {
#     text-align:center;
#     font-size:32px;
#     font-weight:bold;
#     color:white;
#     margin-bottom:20px;
# }

# .pred {
#     font-size:26px;
#     font-weight:bold;
#     text-align:center;
#     color:#00ffcc;
#     margin-top:20px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ===============================
# # Title
# # ===============================
# st.markdown(
#     '<div class="title">🍽️ Restaurant Popularity Predictor</div>',
#     unsafe_allow_html=True
# )

# # ===============================
# # Correct Location Encoding
# # ===============================
# location_map = {
#     "Indore": 7,
#     "Delhi": 4,
#     "Mumbai": 10,
#     "Surat": 14,
#     "Ahmedabad": 0,
#     "Hyderabad": 6,
#     "Bhopal": 2,
#     "Jaipur": 8,
#     "Goa": 5,
#     "Chennai": 3,
#     "Nagpur": 11,
#     "Bangalore": 1,
#     "Pune": 13,
#     "Kochi": 9,
#     "Nashik": 12
# }

# # ===============================
# # UI
# # ===============================
# st.set_page_config(page_title="Restaurant Popularity Predictor", page_icon="🍽️")
# # st.title("🍽️ Restaurant Popularity Predictor")

# location_name = st.selectbox("Select Location", list(location_map.keys()))
# cost = st.number_input("Average Cost", value=300)
# rating = st.number_input("Rating", value=3.5)
# votes = st.number_input("Votes", value=100)
# reviews = st.number_input("Reviews Count", value=50)
# Delivery_Time= st.number_input("Delivery Time", value=0.0)

# # ===============================
# # Prediction
# # ===============================
# if st.button("Predict Popularity"):
#     loc_encoded = location_map[location_name]
    
#     features = np.array([[loc_encoded, cost, rating, votes, reviews, Delivery_Time]])
    
#     pred = model.predict(features)[0]
    
#     st.success(f"Predicted Popularity: {pred}")








import streamlit as st
import numpy as np
import pickle
import os

# ===============================
# Load model safely (pickle)
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

# ===============================
# Page config
# ===============================
st.set_page_config(
    page_title="Restaurant Popularity Predictor",
    page_icon="🍽️",
    layout="centered"
)

# ===============================
# Custom Glass UI Style
# ===============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
}

.card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
}

.title {
    text-align:center;
    font-size:32px;
    font-weight:bold;
    color:white;
    margin-bottom:20px;
}

.pred {
    font-size:26px;
    font-weight:bold;
    text-align:center;
    color:#800080 ;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Title
# ===============================
st.markdown(
    '<div class="title">🍽️ Restaurant Popularity Predictor</div>',
    unsafe_allow_html=True
)

# ===============================
# Input Card
# ===============================
with st.container():
    location_map = {
        "Indore": 7,
        "Delhi": 4,
        "Mumbai": 10,
        "Surat": 14,
        "Ahmedabad": 0,
        "Hyderabad": 6,
        "Bhopal": 2,
        "Jaipur": 8,
        "Goa": 5,
        "Chennai": 3,
        "Nagpur": 11,
        "Bangalore": 1,
        "Pune": 13,
        "Kochi": 9,
        "Nashik": 12
    }

    col1, col2 = st.columns(2)

    with col1:

        location_name = st.selectbox("Select Location", list(location_map.keys()))
        cost = st.number_input("Average Cost", value=300)
        rating = st.number_input("Rating", value=3.5)

    with col2:
        votes = st.number_input("Votes", value=100)
        reviews = st.number_input("Reviews Count", value=50)
        Delivery_Time= st.number_input("Delivery Time", value=0.0)

    # ===============================
    # Prediction
    # ===============================
    if st.button("✨ Predict Popularity"):
        loc_encoded = location_map[location_name]

        features = np.array([[loc_encoded, cost, rating, votes, reviews, Delivery_Time]])

        prediction = model.predict(features)[0]

        st.markdown(
            f'<div class="pred">Predicted Popularity: {prediction}</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

