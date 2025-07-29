import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

app = Flask(__name__)

try:
    model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully.")
except Exception as e:
    print("❌ Failed to load model:", e)
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Salary is ₹{output} Lakhs')
    except Exception as e:
        return render_template('index.html', prediction_text=f'❌ Error: {str(e)}')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    if model is None:
        return jsonify({'error': 'Model not loaded. Check server logs.'})
    
    try:
        data = request.get_json(force=True)
        prediction = model.predict([np.array(list(data.values()))])
        output = prediction[0]
        return jsonify(output)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    print("🔥 Starting Flask app...")
    app.run(debug=True)

