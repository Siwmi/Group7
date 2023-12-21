from flask import Flask, jsonify, request
import numpy as np
from skimage import feature, transform, io
import os
from sklearn.externals import joblib
from joblib import load

app = Flask(__name__)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the model path relative to the script directory
model_path = os.path.join(script_dir, 'saved_model.pkl')

# Load the trained SVM model
clf = joblib.load(model_path)

# Define categories
categories = ['bike', 'cars']

# Function to extract HOG features from an image
def extract_hog_features(image):
    resized_image = transform.resize(image, (64, 64))  # Resize the image to match the training size
    hog_features = feature.hog(resized_image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), transform_sqrt=True)
    return hog_features

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    image = request.files['image'].read()
    image = io.imread(io.BytesIO(image), as_gray=True)

    # Extract HOG features
    hog_features = extract_hog_features(image)

    # Make a prediction
    prediction = clf.predict(np.array([hog_features]))

    # Return the prediction as JSON
    return jsonify({'prediction': categories[prediction[0]]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3300)

