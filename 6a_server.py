"""
Flask server interface running the Emotion Detection Application.
This module handles HTTP routing for the web layout.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Receives text queries via HTTP requests, submits them for evaluation,
    and structures string responses back to the viewport.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Standard Task 6 response output string format
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<strong>{response['dominant_emotion']}</strong>."
    )

@app.route("/")
def render_index_page():
    """
    Renders the default landing home route HTML template user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
