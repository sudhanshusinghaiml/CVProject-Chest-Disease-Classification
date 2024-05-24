"""
This module contains the code that reads the input data from webapp
transforms it as input to prediction pipeline
                OR
It triggers all the training pipeline
"""

import os
from flask import Flask, request, jsonify, render_template
from flask_cors import cross_origin
from src.cnn_classifier.utils.common import decode_image
from src.cnn_classifier.pipeline.prediction_pipeline import PredictionPipeline


os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

# 1. Create the application object
ChestDiseaseClassificationApp = Flask(__name__)
# CORS(app)


class ImagePredictor:
    """Calling PredictionPipeline"""

    def __init__(self):
        self.filename = "inputImage.jpg"
        self.predictor = PredictionPipeline(self.filename)


# 3. Routing to Home Page of "Chest Disease Classification App"
#    (http://127.0.0.1:8000/)
@ChestDiseaseClassificationApp.route("/", methods=["GET"])
@cross_origin()
def home():
    """when a webpage is loaded on webapp it makes of this method by default"""
    return render_template("index.html")


# 3. Expose the Model Training functionality with new set of Data
#    (http://127.0.0.1:8000/train)
@ChestDiseaseClassificationApp.route("/train", methods=["GET", "POST"])
@cross_origin()
def train_route():
    """This method is invoked when user wants to train the model"""
    # os.system("python main.py")
    os.system("dvc repro")
    return "Training done successfully!"


# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted result
#    (http://127.0.0.1:8000/predict)
@ChestDiseaseClassificationApp.route("/predict", methods=["POST"])
@cross_origin()
def predict_route():
    """This method is invoked when user wants to use prediction pipeline"""
    image = request.json["image"]
    classify = ImagePredictor()
    decode_image(image, classify.filename)
    result = classify.predictor.predict()
    return jsonify(result)


# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host='0.0.0.0', port=8080)

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == "__main__":
    # classify = ImagePredictor()
    ChestDiseaseClassificationApp.run(host="0.0.0.0", port=8080, debug=True)
    ChestDiseaseClassificationApp.config["TEMPLATES_AUTO_RELOAD"] = True
