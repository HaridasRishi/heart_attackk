# Original app backup

import numpy as np
import pickle as pkl
from flask import Flask, request, jsonify, render_template

# 1. Initialize Flask app
app = Flask(__name__)

# 2. Load the trained model
try:
    # The 'rb' mode is for reading the file in binary mode
    with open('heart_attack_model.pkl', 'rb') as file:
        model = pkl.load(file)
except FileNotFoundError:
    print("Error: 'heart_attack_model.pkl' not found. Ensure you ran Step 1.")
    model = None

# --- Feature Mapping used by the model ---
# Sex: F -> 0.0, M -> 1.0
# ChestPainType: ASY -> 0.0, ATA -> 1.0, NAP -> 2.0, TA -> 3.0
# RestingECG: LVH -> 0.0, Normal -> 1.0, ST -> 2.0
# ExerciseAngina: N -> 0.0, Y -> 1.0
# ST_Slope: Down -> 0.0, Flat -> 1.0, Up -> 2.0
# ---

@app.route('/')
def home():
    """Renders the HTML form for input."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the prediction request from the frontend."""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500
        
    try:
        # Get data from POST request (form data)
        data = request.form.to_dict()
        
        # Define the feature order expected by the model
        feature_order = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 
                         'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 
                         'Oldpeak', 'ST_Slope']
        
        # Convert and prepare data for prediction, applying the same encoding logic
        features = []
        for key in feature_order:
            value = data[key]
            
            if key == 'Sex':
                features.append(1.0 if value == 'M' else 0.0)
            elif key == 'ChestPainType':
                mapping = {'ASY': 0.0, 'ATA': 1.0, 'NAP': 2.0, 'TA': 3.0}
                features.append(mapping.get(value, 0.0))
            elif key == 'RestingECG':
                mapping = {'LVH': 0.0, 'Normal': 1.0, 'ST': 2.0}
                features.append(mapping.get(value, 1.0))
            elif key == 'ExerciseAngina':
                features.append(1.0 if value == 'Y' else 0.0)
            elif key == 'ST_Slope':
                mapping = {'Down': 0.0, 'Flat': 1.0, 'Up': 2.0}
                features.append(mapping.get(value, 1.0))
            else:
                # Numerical features
                features.append(float(value))

        # Predict the result. Use features (the raw list of floats)
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        
        output = 'Heart Attack Detected' if prediction[0] == 1 else 'Normal'
        
        # Pass the result back to the template
        return render_template('index.html', prediction_text=f'Prediction: {output}')

    except Exception as e:
        # Handle errors gracefully
        return render_template('index.html', prediction_text=f'Error in prediction: {str(e)}')

if __name__ == "__main__":
    # Ensure you have 'heart_attack_model.pkl' in the directory
    # If debug is True, server will restart on code changes
    app.run(debug=True)