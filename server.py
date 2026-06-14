"""Emotion detection Flask application.
This module provides a web interface for the emotion detection functionality.
It handles user input, calls the emotion detection API, and returns formatted results.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """Process the text and return emotion analysis"""
    # Get the text from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Check if the result is valid (None values indicate error)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    # Format the response as required
    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} " 
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
