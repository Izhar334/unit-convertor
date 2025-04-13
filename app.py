import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #1a1a1d;
        color: #ffffff;
    }
    .stApp {
        background-color: #f0fff4;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        text-align: center;
        font-size: 2.5rem;
        color: #0f172a;
        margin-bottom: 1.5rem;
    }
    .stButton > button {
        background: linear-gradient(45deg, #06b6d4, #0ea5e9);
        color: white;
        font-size: 1.125rem;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #fcd34d, #fde68a);
        color: #1a1a1d;
    }
   .result-box {
    font-size: 1.5rem;
    font-weight: 600;
    text-align: center;
    background: linear-gradient(135deg, #0ea5e9, #06b6d4);
    color: #ffffff;
    padding: 20px 30px;
    border-radius: 12px;
    margin-top: 25px;
    box-shadow: 0 8px 25px rgba(14, 165, 233, 0.4);
    border: 2px solid rgba(255, 255, 255, 0.2);
    transition: all 0.3s ease-in-out;
    animation: fadeIn 0.6s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 0.875rem;
        color: #9ca3af;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description

st.markdown(
    "<h1 style='color:#0f172a; text-align:center;'>Effortless Unit Conversion with Streamlit</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#334155;'>Built with Python and Streamlit for a smooth and interactive experience. From meters to miles, kilograms to pounds—convert anything with ease.</p>",
    unsafe_allow_html=True
)


# Sidebar
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Unit Selectors
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Converter Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1_000_000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9 / 5 + 32) if to_unit == "Fahrenheit" else (value + 273.15 if to_unit == "Kelvin" else value)
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5 / 9 if to_unit == "Celsius" else (value - 32) * 5 / 9 + 273.15 if to_unit == "Kelvin" else value)
    elif from_unit == "Kelvin":
        return (value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9 / 5 + 32 if to_unit == "Fahrenheit" else value)
    return value

# Convert Button
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(
        f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown("<div class='footer'>Created by Izhar Ahmed</div>", unsafe_allow_html=True)
