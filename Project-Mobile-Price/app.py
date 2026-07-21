import joblib
import pandas as pd
import streamlit as st

# Load the saved model
model = joblib.load(r"C:\Users\neetu\OneDrive\Desktop\github\Project-Mobile-Price\mobile_price_model.joblib")


PRICE_LABELS = {
    0: "🟢 Low Cost (Under ₹12,000)",
    1: "🟡 Medium Cost (₹12,000–₹20,000)",
    2: "🟠 High Cost (₹20,000–₹35,000)",
    3: "🔴 Very High Cost (₹35,000+)"
}

st.title("📱 Mobile Price Predictor")
st.write("Enter the phone specs to predict its price range.")

# Input fields
battery  = st.number_input("Battery Power (mAh)", 500, 5000, 1500)
ram      = st.number_input("RAM (MB)", 256, 4000, 2000)
px_h     = st.number_input("Pixel Height", 0, 1960, 1080)
px_w     = st.number_input("Pixel Width", 500, 2000, 1920)
int_mem  = st.number_input("Internal Memory (GB)", 2, 256, 32)
n_cores  = st.slider("Number of CPU Cores", 1, 8, 4)
pc       = st.number_input("Primary Camera (MP)", 0, 64, 12)
fc       = st.number_input("Front Camera (MP)", 0, 40, 8)
mobile_wt = st.number_input("Weight (g)", 80, 300, 150)
sc_h     = st.number_input("Screen Height (cm)", 5, 20, 15)
sc_w     = st.number_input("Screen Width (cm)", 0, 18, 7)
talk_time = st.number_input("Talk Time (hrs)", 2, 24, 10)
clock    = st.slider("Clock Speed (GHz)", 0.5, 3.0, 1.5)
m_dep    = st.number_input("Phone Depth (cm)", 0.1, 1.0, 0.5)
blue     = st.checkbox("Bluetooth")
dual_sim = st.checkbox("Dual SIM")
four_g   = st.checkbox("4G")
three_g  = st.checkbox("3G", value=True)
touch    = st.checkbox("Touch Screen", value=True)
wifi     = st.checkbox("WiFi", value=True)

if st.button("Predict Price Range", type="primary"):
    # Build input in same column order your model was trained on
    input_data = pd.DataFrame([{
        "battery_power": battery,
        "blue":          int(blue),
        "clock_speed":   clock,
        "dual_sim":      int(dual_sim),
        "fc":            fc,
        "four_g":        int(four_g),
        "int_memory":    int_mem,
        "m_dep":         m_dep,
        "mobile_wt":     mobile_wt,
        "n_cores":       n_cores,
        "pc":            pc,
        "px_height":     px_h,
        "px_width":      px_w,
        "ram":           ram,
        "sc_h":          sc_h,
        "sc_w":          sc_w,
        "talk_time":     talk_time,
        "three_g":       int(three_g),
        "touch_screen":  int(touch),
        "wifi":          int(wifi),
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"### {PRICE_LABELS[prediction]}")