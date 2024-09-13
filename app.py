import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load(r"H:\CampusX_DS\week43 - My Projects Aug 2024\mlops_laptop_price_prediction\artifacts\model.pkl")
preprocessor = joblib.load(r"H:\CampusX_DS\week43 - My Projects Aug 2024\mlops_laptop_price_prediction\artifacts\preprocessor.pkl")


# Path to the Excel file
excel_path = "H:/CampusX_DS/week43 - My Projects Aug 2024/mlops_laptop_price_prediction/notebook/smartprix_laptop_cleaned_v8.xlsx"

# Read the Excel file
def load_dropdown_options(file_path):
    df = pd.read_excel(file_path, sheet_name=None)  # Load all sheets
    options = {}
    
    # Iterate through all sheets and collect unique values for each relevant column
    for sheet_name, sheet_df in df.items():
        if 'brand' in sheet_df.columns:
            options['brand'] = sheet_df['brand'].dropna().unique()
        if 'os' in sheet_df.columns:
            options['os'] = sheet_df['os'].dropna().unique()
        if 'processor_brand' in sheet_df.columns:
            options['processor_brand'] = sheet_df['processor_brand'].dropna().unique()
        if 'ram_type' in sheet_df.columns:
            options['ram_type'] = sheet_df['ram_type'].dropna().unique()
        if 'memory_type' in sheet_df.columns:
            options['memory_type'] = sheet_df['memory_type'].dropna().unique()
        if 'graphics_card_brand' in sheet_df.columns:
            options['graphics_card_brand'] = sheet_df['graphics_card_brand'].dropna().unique()
    
    return options

# Load options from Excel file
options = load_dropdown_options(excel_path)

# Define the prediction function
def predict_price(features):
    # Convert input features to a DataFrame
    features_df = pd.DataFrame([features])
    print(features_df)
    # Apply preprocessing
    processed_features = preprocessor.transform(features_df)
    # Predict the price
    predicted_price = model.predict(processed_features)
    print(predicted_price)
    return predicted_price[0]


# Streamlit app
st.title('Laptop Price Prediction')

st.sidebar.header('Input Features')


# Define input fields with options loaded from the Excel file
rating = st.sidebar.slider('Rating', 0.0, 5.0, 4.0)
specScore = st.sidebar.slider('Specification Score', 0, 100, 85)
brand = st.sidebar.selectbox('Brand', options.get('brand', ['Brand1']))  # Default to 'Brand1' if options are not available
threads = st.sidebar.slider('Threads', 1, 16, 4)
screen_size = st.sidebar.slider('Screen Size (inches)', 10.0, 20.0, 15.6)
os = st.sidebar.selectbox('Operating System', options.get('os', ['Windows']))  # Default to 'Windows' if options are not available
warranty = st.sidebar.slider('Warranty (years)', 0, 5, 1)
core_count = st.sidebar.slider('Core Count', 1, 16, 4)
processor_brand = st.sidebar.selectbox('Processor Brand', options.get('processor_brand', ['Intel']))  # Default to 'Intel' if options are not available
ram_capacity = st.sidebar.slider('RAM Capacity (GB)', 4, 64, 8)
ram_type = st.sidebar.selectbox('RAM Type', options.get('ram_type', ['DDR4']))  # Default to 'DDR4' if options are not available
memory_capacity = st.sidebar.slider('Memory Capacity (GB)', 128, 2048, 512)
memory_type = st.sidebar.selectbox('Memory Type', options.get('memory_type', ['SSD']))  # Default to 'SSD' if options are not available
graphics_card_brand = st.sidebar.selectbox('Graphics Card Brand', options.get('graphics_card_brand', ['NVIDIA']))  # Default to 'NVIDIA' if options are not available
PPI = st.sidebar.slider('PPI', 100, 300, 141)

# Collect all inputs into a dictionary
features = {
    'rating': rating,
    'specScore': specScore,
    'brand': brand,
    'threads': threads,
    'screen_size': screen_size,
    'os': os,
    'warranty': warranty,
    'core_count': core_count,
    'processor_brand': processor_brand,
    'ram_capacity': ram_capacity,
    'ram_type': ram_type,
    'memory_capacity': memory_capacity,
    'memory_type': memory_type,
    'graphics_card_brand': graphics_card_brand,
    'PPI': PPI
}

# Prediction
if st.sidebar.button('Predict'):
    price = predict_price(features)
    st.write(f'The estimated price of the laptop is: ₹{price:.2f}')

st.markdown("""
### Instructions:
1. Adjust the sliders and select options on the sidebar to input the laptop specifications.
2. Click the "Predict" button to see the estimated price of the laptop based on the input features.
""")