from flask import Flask, request, jsonify
import numpy as np

def create_app(model, scaler):
    app = Flask(__name__)

    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.json.get('data', None)
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            input_data = np.array(data).reshape(1, -1)
            scaled_data = scaler.transform(input_data)
            prediction = model.predict(scaled_data)[0]
            probability = model.predict_proba(scaled_data)[0, 1]
            return jsonify({'prediction': int(prediction), 'probability': float(probability)})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app
