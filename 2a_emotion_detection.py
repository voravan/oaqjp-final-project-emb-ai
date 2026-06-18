"""
This module communicates with the Watson NLP Emotion Detection service to analyze text inputs.
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    Sends input text to the Watson NLP Emotion Detection API and returns parsed emotion scores.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send POST request to the Watson NLP service
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    
    # Parse the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion values
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']
    
    # Determine the dominant emotion programmatically
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    # Return the formatted output dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
